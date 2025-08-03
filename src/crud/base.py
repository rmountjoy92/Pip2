from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union, Callable

from pydantic import BaseModel
from sqlalchemy import func, null, and_, or_
from sqlalchemy.orm import Session, Query

from src.database.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def query(self, db: Session):
        return db.query(self.model)

    def get(self, db: Session, model_id: Any) -> Optional[ModelType]:
        return db.query(self.model).get(model_id)

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.model(**obj_in.dict(exclude_unset=True))
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> ModelType:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict()
        for key, value in update_data.items():
            if value is not None:
                setattr(db_obj, key, value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, model_id: int = None) -> ModelType:
        obj = db.query(self.model).get(model_id)
        db.delete(obj)
        db.commit()
        return obj

    def paginate(
        self,
        db: Session,
        *,
        query_func: Callable = None,
        query: Query = None,
        page: int = 1,
        limit: int = 20,
    ) -> Dict:
        if not query:
            query = db.query(self.model)
            query = query_func(query)
        total = self.count(query=query)
        if page == 1:
            offset = 0
        else:
            pm = page - 1
            offset = pm * limit
        records = query.offset(offset).limit(limit).all()
        return {"items": records, "page": page, "size": limit, "total": total}

    def count(
        self, db: Session = None, query_func: Callable = None, query: Query = None
    ):
        if not query:
            query = db.query(self.model)
            query = query_func(query)
        count_query = query.statement.with_only_columns([func.count()]).order_by(None)
        count = query.session.execute(count_query).scalar()
        return count

    def get_where(self, db: Session, **filters) -> List[ModelType]:
        """
        Retrieve records based on multiple filter conditions.
        **Parameters**
        * `filters`: Dictionary of field names and their values for filtering.
        """
        query = db.query(self.model).filter_by(**filters)
        return query.all()

    def get_first_where(self, db: Session, **filters) -> Optional[ModelType]:
        """
        Retrieve the first record based on multiple filter conditions.
        **Parameters**
        * `filters`: Dictionary of field names and their values for filtering.
        """
        query = db.query(self.model).filter_by(**filters)
        return query.first()

    def get_by_field(self, db: Session, field_name: str, value: Any) -> List[ModelType]:
        """
        Retrieve records where a specific field matches a value.
        **Parameters**
        * `field_name`: Name of the field in the model to filter by.
        * `value`: Value that the field should match.
        """
        field = getattr(self.model, field_name, None)
        if not field:
            raise AttributeError(
                f"{field_name} is not a valid field of {self.model.__name__}"
            )
        query = db.query(self.model).filter(field == value)
        return query.all()

    def get_multi_filter(
        self, db: Session, filters: Dict[str, Any], conjunction: str = "and"
    ) -> List[ModelType]:
        """
        Retrieve records based on multiple filters with 'and'/'or' conjunction.
        **Parameters**
        * `filters`: Dictionary of field names and their values.
        * `conjunction`: Either "and" or "or" to combine filters.
        """
        conditions = [
            getattr(self.model, field) == value
            for field, value in filters.items()
            if getattr(self.model, field, None) is not None
        ]
        if conjunction == "or":
            query = db.query(self.model).filter(or_(*conditions))
        else:
            query = db.query(self.model).filter(and_(*conditions))
        return query.all()

    def get_where_null(self, db: Session, *columns: str) -> List[ModelType]:
        """
        Retrieve records where specified columns are null.
        **Parameters**
        * `columns`: List of column names to check for null values.
        """
        conditions = [getattr(self.model, column) == null() for column in columns]
        query = db.query(self.model).filter(*conditions)
        return query.all()

    def get_where_not_null(self, db: Session, *columns: str) -> List[ModelType]:
        """
        Retrieve records where specified columns are not null.
        **Parameters**
        * `columns`: List of column names to check for non-null values.
        """
        conditions = [getattr(self.model, column) != null() for column in columns]
        query = db.query(self.model).filter(*conditions)
        return query.all()
