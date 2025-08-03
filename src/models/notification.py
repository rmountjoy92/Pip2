from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime

from src.database.base_class import Base
from src.database.session import engine


class Notification(Base):
    __tablename__ = "notification"

    id = Column(Integer, primary_key=True, index=True)
    emoji = Column(String(25), nullable=False)
    title = Column(String(255), nullable=False)
    subtitle = Column(String(255))
    priority = Column(Integer, default=0)
    is_dismissed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
    dismissed_at = Column(DateTime)

    def for_pip(self):
        return {
            "id": self.id,
            "emoji": self.emoji,
            "title": self.title,
            "subtitle": self.subtitle,
            "priority": self.priority,
            "is_dismissed": self.is_dismissed,
            "created_at": self.created_at.isoformat(),
            "dismissed_at": (
                self.dismissed_at.isoformat() if self.dismissed_at is not None else None
            ),
        }


Base.metadata.create_all(engine)
