from typing import Any, List, Dict

def validate_input(value: Any) -> bool:
    """Validate a single input value."""
    if value is None:
        return False
    if isinstance(value, str):
        if not value.strip():
            return False
        # Check for invalid characters, e.g. only letters and spaces
        if not all(c.isalnum() or c.isspace() for c in value):
            return False
    elif isinstance(value, (int, float)):
        if value < 0:
            return False
    else:
        return False
    return True

def process_item(item: Any) -> Any:
    """Process a single validated item."""
    if isinstance(item, str):
        return item.strip().upper()
    elif isinstance(item, (int, float)):
        return item * 2
    return item

def main_processing_loop(data: List[Any]) -> Dict[str, List[Any]]:
    """Main processing loop with input validation."""
    valid_items = []
    invalid_items = []
    for idx, item in enumerate(data):
        # Perform input validation before processing
        if not validate_input(item):
            invalid_items.append({"index": idx, "value": item})
            continue
        # Process the valid item
        processed = process_item(item)
        valid_items.append(processed)
        # Additional logging or steps
        if idx % 2 == 0:
            # simulate some conditional step
            pass
    return {
        "processed": valid_items,
        "invalid": invalid_items
    }

# Sample data for demonstration
SAMPLE_DATA = [42, "hello world", -1, "Test123", "", 3.14, "valid input", None, "another"]

if __name__ == "__main__":
    print("Starting main processing...")
    results = main_processing_loop(SAMPLE_DATA)
    print("Processed items:", results["processed"])
    print("Invalid items:", results["invalid"])
    print("Processing complete.")
