import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads configuration from a JSON file with fallback defaults."""
    config = defaults.copy()
    
    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                config.update(data)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

if __name__ == '__main__':
    # Example usage
    default_settings = {
        "host": "localhost",
        "port": 8080,
        "debug": False
    }
    
    # Attempt to load from local file, merge with defaults
    active_config = load_config("settings.json", default_settings)
    print(f"Config loaded: {active_config}")