import functools
from typing import Callable, Any, Dict

# Cache for computed processor results to avoid redundant calculations
_memoization_cache: Dict[tuple, Any] = {}

def memoize_processor(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

class DataProcessor:
    """Core processing engine with optimized computation paths."""

    def __init__(self, settings: Dict[str, Any] = None):
        self.settings = settings or {}

    @memoize_processor
    def compute_heavy_metric(self, data_points: tuple) -> float:
        """Performs expensive mathematical aggregation on data points."""
        if not data_points:
            return 0.0
        
        # Using generator expression for memory efficiency
        return sum(x * 1.05 for x in data_points) / len(data_points)

    def clear_cache(self) -> None:
        """Resets the memoization store."""
        _memoization_cache.clear()