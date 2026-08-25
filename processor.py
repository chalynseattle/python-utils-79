import re
def is_valid_input(item):
    """Check if input is valid: non-empty str, alnum+space, 1-50 chars."""
    if not isinstance(item, str):
        return False
    item = item.strip()
    if not item or len(item) > 50:
        return False
    if not re.match(r'^[a-zA-Z0-9\s]+$', item):
        return False
    return True

def process_item(item):
    """Process valid item: return uppercased version."""
    return item.strip().upper()

def main_processing_loop(inputs):
    """Main loop: validate each input then process if valid."""
    results = []
    for raw in inputs:
        if is_valid_input(raw):
            processed = process_item(raw)
            results.append(processed)
            print("Processed:", processed)
        else:
            print("Skipped invalid:", raw)
    return results

if __name__ == "__main__":
    test_inputs = ["hello", "world123", "bad@input", "valid entry", "x"*60, ""]
    print("Running main processing loop with validation")
    output = main_processing_loop(test_inputs)
    print("Done. Results count:", len(output))