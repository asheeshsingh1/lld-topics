from abc import ABC, abstractmethod
from log_message import LogMessage
from log_level import LogLevel

class LogFilter(ABC):
    @abstractmethod
    def should_log(self, message: LogMessage) -> bool:
        pass

    @abstractmethod
    def set_level(self, level: LogLevel):
        pass

    @abstractmethod
    def get_level(self) -> LogLevel:
        pass