from typing import List

from sqlalchemy.orm import Session

from src.crud.base import CRUDBase, CreateSchemaType, ModelType
from src.models.notification import Notification
from src.schemas import NotificationCreate, NotificationUpdate


class CRUDNotification(CRUDBase[Notification, NotificationCreate, NotificationUpdate]):
    def create(self, db: Session, *, obj_in: NotificationCreate) -> ModelType:
        if not obj_in.emoji:
            obj_in.emoji = "✅"
        return super().create(db, obj_in=obj_in)

    def get_multi(
        self,
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
        exclude_dismissed: bool = True
    ) -> List[Notification]:
        if exclude_dismissed:
            return (
                db.query(self.model)
                .filter_by(is_dismissed=False)
                .order_by(self.model.priority.desc(), self.model.created_at.desc())
                .offset(skip)
                .limit(limit)
                .all()
            )
        return db.query(self.model).offset(skip).limit(limit).all()


notification = CRUDNotification(Notification)
