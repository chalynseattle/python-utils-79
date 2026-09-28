import logging
from typing import Any, Optional, Callable

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """Execute a function with robust error handling for common edge cases."""
    try:
        if not callable(func):
            raise ValueError("Provided object is not callable")
        return func(*args, **kwargs)
    except (ValueError, TypeError, AttributeError) as e:
        logger.error(f"Invalid operation detected: {e}")
    except Exception as e:
        logger.critical(f"Unexpected runtime failure: {e}")
    return default

def parse_int_safe(value: Any, default: int = 0) -> int:
    """Convert input to integer with fallback for non-numeric types."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default

def get_nested_key(data: dict, path: str, delimiter: str = ".") -> Optional[Any]:
    """Retrieve value from nested dictionary using dot notation path."""
    if not isinstance(data, dict):
        return None
    
    keys = path.split(delimiter)
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return None