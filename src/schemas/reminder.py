from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ReminderCreateRequest(BaseModel):
    title: str = Field(..., description="The reminder title.")
    subtitle: Optional[str] = Field(None, description="The reminder subtitle.")
    priority: Optional[int] = Field(
        0, description="The reminder priority, accepted values: 0,1,2,3,4."
    )
    time: datetime = Field(
        ..., description="The time the reminder will create a notification."
    )
    cron_expression: Optional[str] = Field(
        None, description="A cron expression for when the reminder will repeat."
    )


class ReminderBase(BaseModel):
    pass


class ReminderCreate(ReminderBase):
    title: str
    subtitle: Optional[str] = None
    priority: Optional[int] = 0
    time: datetime
    cron_expression: Optional[str] = None


class ReminderUpdate(ReminderBase):
    pass


class ReminderResponse(ReminderBase):
    id: int
    title: str
    subtitle: Optional[str] = None
    priority: Optional[int] = 0
    created_at: datetime

    class Config:
        from_attributes = True
