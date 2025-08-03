from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class NotificationCreateRequest(BaseModel):
    title: str = Field(..., description="The notification title.")
    emoji: Optional[str] = Field(None, description="The notification emoji.")
    subtitle: Optional[str] = Field(None, description="The notification subtitle.")
    priority: Optional[int] = Field(
        0, description="The notification priority, accepted values: 0,1,2,3,4."
    )


class NotificationBase(BaseModel):
    pass


class NotificationCreate(NotificationBase):
    title: str
    emoji: str
    subtitle: Optional[str] = None
    priority: Optional[int] = 0


class NotificationUpdate(NotificationBase):
    is_dismissed: bool
    dismissed_at: datetime


class NotificationResponse(NotificationBase):
    id: int
    emoji: str
    title: str
    subtitle: Optional[str] = None
    priority: Optional[int] = 0
    is_dismissed: Optional[bool]
    created_at: datetime
    dismissed_at: Optional[datetime] = None

    class Config:
        from_attributes = True
