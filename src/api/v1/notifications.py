from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from src import crud
from src.sockets import socket
from src.api.deps import get_db
from src.models import Notification
from src.schemas import (
    NotificationCreateRequest,
    NotificationResponse,
    Message,
    NotificationUpdate,
)

router = APIRouter()


@router.post("", summary="create a notification", response_model=NotificationResponse)
async def create_notification(
    req: NotificationCreateRequest,
    db: Session = Depends(get_db),
):
    n: Notification = crud.notification.create(db, obj_in=req)
    await socket.manager.emit("notification-created", n.for_pip())
    return n


@router.get(
    "", summary="get all notifications", response_model=List[NotificationResponse]
)
def read_notifications(
    db: Session = Depends(get_db),
    exclude_dismissed: bool = True,
):
    """
    Retrieve all notifications.
    """
    notifications = crud.notification.get_multi(db, exclude_dismissed=exclude_dismissed)
    return notifications


@router.post(
    "/{notification_id}/dismiss",
    summary="dismiss a notification",
    response_model=Message,
)
async def dismiss_notification(
    notification_id: int,
    db: Session = Depends(get_db),
):
    notification = crud.notification.get(db, model_id=notification_id)
    if not notification:
        raise HTTPException(status_code=404, detail="notification not found")
    crud.notification.update(
        db,
        db_obj=notification,
        obj_in=NotificationUpdate(is_dismissed=True, dismissed_at=datetime.now()),
    )
    await socket.manager.emit("notification-dismissed", {"id": notification_id})
    return Message(message="Done.")
