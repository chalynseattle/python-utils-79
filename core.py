from typing import Any, Dict, List, Optional, Union

def merge_configs(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries for configuration management."""
    merged = base.copy()
    for key, value in override.items():
        if isinstance(value, dict) and key in merged and isinstance(merged[key], dict):
            merged[key] = merge_configs(merged[key], value)
        else:
            merged[key] = value
    return merged

def format_data_list(data: List[Any], prefix: str = "Item") -> List[str]:
    """Convert list items to strings with prefixed numbering."""
    return [f"{prefix} {i+1}: {str(item)}" for i, item in enumerate(data)]

def filter_by_type(items: List[Any], target_type: type) -> List[Any]:
    """Extract items matching a specific type from a list."""
    return [item for item in items if isinstance(item, target_type)]

class DataProcessor:
    """Utility class for standardizing input data formats."""
    def __init__(self, debug: bool = False) -> None:
        self.debug = debug

    def process(self, payload: Union[str, int]) -> str:
        """Sanitize and convert input to a standardized string."""
        if self.debug:
            print(f"Processing: {payload}")
        return str(payload).strip().lower()