import logging
import sys
from typing import Optional

class AppLogger:
    """Standardized logging utility for python-utils-79"""
    
    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        if not self.logger.handlers:
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def error(self, msg: str, exc_info: bool = False) -> None:
        self.logger.error(msg, exc_info=exc_info)

    @classmethod
    def get_logger(cls, name: str = "python-utils-79") -> logging.Logger:
        return cls(name).logger

def get_configured_logger(name: str) -> logging.Logger:
    """Factory function for consistent module logging"""
    return AppLogger.get_logger(name)