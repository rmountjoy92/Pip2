from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from src.database.base_class import Base


class ReminderCategory(Base):
    __tablename__ = "reminder_categories"

    id = Column(Integer, primary_key=True, index=True)
    emoji = Column(String(25), nullable=False)
    name = Column(String(255), nullable=False)
    priority = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now())

    def for_pip(self):
        return {
            "id": self.id,
            "emoji": self.emoji,
            "name": self.name,
            "priority": self.priority,
            "created_at": self.created_at.isoformat(),
        }
