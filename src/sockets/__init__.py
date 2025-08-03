import json
from typing import TypeVar, Any

from fastapi_socketio import SocketManager
from pydantic import BaseModel

from src.database.base_class import Base
from .events import init_events

ObjectSchema = TypeVar("ObjectSchema", bound=BaseModel)
DbObject = TypeVar("DbObject", bound=Base)


class Socket:
    manager = None

    def init_manager(self, app: Any):
        self.manager = SocketManager(app=app, socketio_path="/ws/socket.io")
        init_events(self.manager)

    async def emit_db_object(
        self,
        *,
        subject: str = None,
        room: str = None,
        response_model: ObjectSchema = None,
        db_obj: DbObject = None
    ) -> None:
        json_payload = json.loads(response_model.from_orm(db_obj).json())
        return await self.manager.emit(subject, json_payload, room=room)


socket = Socket()
