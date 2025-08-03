from enum import Enum


class NotificationTypes(str, Enum):
    ERROR = "error"
    WARNING = "warning"
    REMINDER = "reminder"
    INFO = "info"
    SUCCESS = "success"
