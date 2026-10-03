import datetime
from typing import Any, Dict, Optional


class BaseUtilsError(Exception):
    """Base exception class for python-utils-79 with context tracking for edge cases."""

    def __init__(
        self, message: str, context: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(message)
        self.message = message
        self.timestamp = datetime.datetime.now(datetime.timezone.utc)
        self.context = context or {}

    def to_dict(self) -> Dict[str, Any]:
        """Serializes the error and its context for structured logging or API responses."""
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "timestamp": self.timestamp.isoformat(),
            "context": self.context,
        }

    def __str__(self) -> str:
        if self.context:
            return f"{self.message} (Context: {self.context})"
        return self.message


class ValidationError(BaseUtilsError):
    """Raised when data validation fails during utility operations."""


class ConfigurationError(BaseUtilsError):
    """Raised when system or environment configuration is invalid or missing."""


class ProcessingError(BaseUtilsError):
    """Raised when an operation fails during runtime processing."""


def wrap_exception(
    exc: Exception, context: Optional[Dict[str, Any]] = None
) -> ProcessingError:
    """Helper to wrap standard Python exceptions into context-aware ProcessingErrors."""
    error_msg = f"Underlying exception: {type(exc).__name__} - {str(exc)}"
    ctx = context or {}
    ctx["original_exception"] = type(exc).__name__
    return ProcessingError(error_msg, context=ctx)
