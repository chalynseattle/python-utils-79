import json
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def safe_load_json(file_path: str) -> Dict[str, Any]:
    """Load and parse JSON file with error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"failed to load json from {file_path}: {e}")
        return {}

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten nested dictionary structure."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def get_nested(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Access nested dictionary keys using dot notation."""
    keys = path.split('.')
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data

def chunk_list(data: list, size: int):
    """Split list into chunks of specific size."""
    for i in range(0, len(data), size):
        yield data[i:i + size]