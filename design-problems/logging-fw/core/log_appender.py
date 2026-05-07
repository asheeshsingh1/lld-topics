from abc import ABC, abstractmethod
from typing import List
from core.log_level import LogLevel
from core.log_message import LogMessage
from core.log_formatter import LogFormatter

class LogAppender(ABC):
    @abstractmethod
    def append(self, message: LogMessage):
        pass

    @abstractmethod
    def set_level(self, level: LogLevel):
        pass

    @abstractmethod
    def get_level(self) -> LogLevel:
        pass

    @abstractmethod
    def is_enabled(self, level: LogLevel) -> bool:
        pass

    @abstractmethod
    def set_formatter(self, formatter: 'LogFormatter'):
        pass

    @abstractmethod
    def get_formatter(self) -> 'LogFormatter':
        pass