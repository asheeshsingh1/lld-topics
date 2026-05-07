from dataclasses import dataclass, field
from datetime import datetime
from core.log_level import LogLevel

@dataclass(frozen=True)
class LogMessage:
    level: LogLevel
    message: str
    timestamp: datetime = field(default_factory=datetime.now)
    source: str = "Unknown"

    def __str__(self):
        return f"LogMessage{{level={self.level}, message='{self.message}', source='{self.source}'}}"

class LogMessageBuilder:
    def __init__(self):
        self._level = None
        self._message = None
        self._timestamp = datetime.now()
        self._source = "Unknown"

    def level(self, level: LogLevel):
        self._level = level
        return self

    def message(self, message: str):
        self._message = message
        return self

    def source(self, source: str):
        self._source = source
        return self

    def timestamp(self, timestamp: datetime):
        self._timestamp = timestamp
        return self

    def build(self) -> LogMessage:
        if self._level is None:
            raise ValueError("LogLevel is required")
        if not self._message:
            raise ValueError("Message is required")
        return LogMessage(
            level=self._level,
            message=self._message,
            timestamp=self._timestamp,
            source=self._source
        )