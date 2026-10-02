import logging

# Configure basic logging for the processor
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures input is a non-empty dictionary with required keys."""
    if not isinstance(data, dict):
        return False
    if 'id' not in data or 'payload' not in data:
        return False
    return True

def process_items(items):
    """Iterates through items and performs validation before execution."""
    for index, item in enumerate(items):
        if not validate_input(item):
            logger.warning(f"Skipping invalid item at index {index}: {item}")
            continue

        try:
            # Simulate core processing logic
            result = f"Processed ID {item['id']}: {item['payload']}"
            logger.info(result)
        except Exception as e:
            logger.error(f"Unexpected error processing item {index}: {e}")

if __name__ == "__main__":
    # Mock input stream
    data_stream = [
        {"id": 1, "payload": "data_a"},
        {"invalid": "structure"},
        {"id": 2, "payload": "data_b"},
        None
    ]
    process_items(data_stream)