import logging
import sys

def setup_logger(name: str):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

def process_data(data_stream):
    logger = setup_logger('processor')
    
    for entry in data_stream:
        # Validate input structure
        if not isinstance(entry, dict) or 'id' not in entry:
            logger.error(f'invalid input format received: {entry}')
            continue
            
        # Validate specific value constraints
        value = entry.get('value')
        if not isinstance(value, (int, float)) or value < 0:
            logger.warning(f'skipping invalid numeric value: {value}')
            continue
            
        try:
            # Process valid entry
            processed = value * 2
            logger.info(f'processed item {entry["id"]}: {processed}')
        except Exception as e:
            logger.exception(f'unexpected error during processing: {e}')

if __name__ == '__main__':
    sample_data = [{'id': 1, 'value': 10}, {'id': 2, 'value': -5}, 'bad_data', {'id': 3, 'value': 20}]
    process_data(sample_data)