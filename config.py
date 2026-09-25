import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles configuration loading from JSON with fallback defaults."""
    
    def __init__(self, default_config: Dict[str, Any]):
        self.defaults = default_config
        self.config = default_config.copy()

    def load_from_file(self, filepath: str) -> None:
        """Updates config with data from a JSON file."""
        if not os.path.exists(filepath):
            return
        
        try:
            with open(filepath, 'r') as f:
                file_data = json.load(f)
                self.config.update(file_data)
        except (json.JSONDecodeError, IOError):
            pass

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves value or returns provided/internal default."""
        return self.config.get(key, default if default is not None else self.defaults.get(key))

def get_config(filepath: str, defaults: Dict[str, Any]) -> ConfigLoader:
    """Factory function for creating a populated loader."""
    loader = ConfigLoader(defaults)
    loader.load_from_file(filepath)
    return loader