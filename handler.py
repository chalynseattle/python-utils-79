import logging

# Configure logger for module tracking
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures input is a non-empty dictionary with required keys."""
    if not isinstance(data, dict):
        return False
    if 'task_id' not in data or 'payload' not in data:
        return False
    return True

def process_items(items):
    """
    Main processing loop with integrated input validation.
    Processes a list of items and skips malformed records.
    """
    results = []
    for index, item in enumerate(items):
        if not validate_input(item):
            logger.warning(f"Skipping malformed input at index {index}")
            continue
        
        try:
            # Simulate core processing logic
            processed_val = str(item['payload']).upper()
            results.append({
                "id": item['task_id'],
                "data": processed_val
            })
        except Exception as e:
            logger.error(f"Processing error at index {index}: {e}")
            
    return results

if __name__ == "__main__":
    data_stream = [
        {"task_id": 1, "payload": "hello"},
        {"invalid": "data"},
        {"task_id": 2, "payload": "world"}
    ]
    processed = process_items(data_stream)
    print(f"Final output count: {len(processed)}")