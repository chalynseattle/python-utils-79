import collections.abc
from typing import Any, Dict, List, Optional

def deep_flatten(items: Any) -> List[Any]:
    """Recursively flatten nested lists or tuples into a single list."""
    flat = []
    for item in items:
        if isinstance(item, (list, tuple)):
            flat.extend(deep_flatten(item))
        else:
            flat.append(item)
    return flat

def merge_dicts(dict1: Dict, dict2: Dict, deep: bool = False) -> Dict:
    """Merge two dictionaries; optional recursive merge for nested keys."""
    result = dict1.copy()
    for key, value in dict2.items():
        if deep and key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value, deep=True)
        else:
            result[key] = value
    return result

def filter_none(data: Dict) -> Dict:
    """Remove all keys with None values from a dictionary."""
    return {k: v for k, v in data.items() if v is not None}

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of a specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be a positive integer")
    return [items[i:i + size] for i in range(0, len(items), size)]