from typing import Any, Union, List, Dict

def _parse_path(path: Union[str, List[Union[str, int]]]) -> List[Union[str, int]]:
    """Helper to parse dot-separated string paths or return lists as-is."""
    if isinstance(path, str):
        parts = []
        for part in path.split('.'):
            if part.isdigit():
                parts.append(int(part))
            else:
                parts.append(part)
        return parts
    return list(path)

def get_nested(data: Union[Dict, List], path: Union[str, List[Union[str, int]]], default: Any = None) -> Any:
    """
    Safely retrieve a value from a nested dictionary or list using a path.
    Example: get_nested(data, "users.0.name") or get_nested(data, ["users", 0, "name"])
    """
    keys = _parse_path(path)
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list) and isinstance(key, int):
            try:
                current = current[key]
            except IndexError:
                return default
        else:
            return default
    return current

def set_nested(data: Union[Dict, List], path: Union[str, List[Union[str, int]]], value: Any) -> bool:
    """
    Set a value in a nested dictionary or list, mutating the structure in-place.
    Returns True if successfully set, False otherwise.
    """
    keys = _parse_path(path)
    if not keys:
        return False
    
    current = data
    for i, key in enumerate(keys[:-1]):
        next_key = keys[i + 1]
        if isinstance(current, dict):
            if key not in current:
                current[key] = [] if isinstance(next_key, int) else {}
            current = current[key]
        elif isinstance(current, list) and isinstance(key, int):
            while len(current) <= key:
                current.append(None)
            if current[key] is None:
                current[key] = [] if isinstance(next_key, int) else {}
            current = current[key]
        else:
            return False

    last_key = keys[-1]
    if isinstance(current, dict):
        current[last_key] = value
        return True
    elif isinstance(current, list) and isinstance(last_key, int):
        while len(current) <= last_key:
            current.append(None)
        current[last_key] = value
        return True
    return False