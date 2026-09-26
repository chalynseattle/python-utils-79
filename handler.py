import logging
import os
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class DataHandler:
    """Manages data processing and cleanup cycles."""
    def __init__(self, directory: str = "./data"):
        self.directory = directory
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def process_payload(self, data: Dict[str, Any]) -> bool:
        """Validates and saves payload to storage."""
        try:
            if not data or "id" not in data:
                return False
            
            filepath = os.path.join(self.directory, f"{data['id']}.json")
            with open(filepath, "w") as f:
                import json
                json.dump(data, f)
            return True
        except (IOError, TypeError) as e:
            logger.error(f"failed to process payload: {e}")
            return False

    def purge_old_data(self, max_files: int = 100) -> int:
        """Removes excess files from the storage directory."""
        files = sorted(
            [os.path.join(self.directory, f) for f in os.listdir(self.directory)],
            key=os.path.getmtime
        )

        deleted_count = 0
        while len(files) > max_files:
            file_to_remove = files.pop(0)
            os.remove(file_to_remove)
            deleted_count += 1
        
        return deleted_count