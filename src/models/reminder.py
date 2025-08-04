from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from src.database.base_class import Base


class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    subtitle = Column(String(255))
    priority = Column(Integer, default=0)
    time = Column(DateTime, nullable=False)
    cron_expression = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())

    def for_pip(self):
        return {
            "id": self.id,
            "title": self.title,
            "subtitle": self.subtitle,
            "priority": self.priority,
            "time": self.time.isoformat(),
            "cron_expression": self.cron_expression,
            "created_at": self.created_at.isoformat(),
        }
