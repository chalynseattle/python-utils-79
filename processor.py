import logging

logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures input is a non-empty dictionary."""
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    if not data:
        raise ValueError("Input data cannot be empty")
    return True

def process_items(items):
    """Main processing loop with validation."""
    results = []
    for item in items:
        try:
            if validate_input(item):
                # Simulate core processing logic
                processed = {k: str(v).upper() for k, v in item.items()}
                results.append(processed)
        except (ValueError, TypeError) as e:
            logger.error(f"Skipping invalid item {item}: {e}")
            continue
    return results

if __name__ == "__main__":
    data_batch = [{"id": 1, "val": "a"}, {}, "invalid", {"id": 2, "val": "b"}]
    output = process_items(data_batch)
    print(f"Processed {len(output)} items successfully.")