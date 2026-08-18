import json

class InputError(Exception):
    pass

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def validate_input(self):
        if not isinstance(self.data, dict):
            raise InputError('Input must be a dictionary')
        if 'name' not in self.data or 'value' not in self.data:
            raise InputError('Missing required fields: name and value')
        if not isinstance(self.data['value'], (int, float)):
            raise InputError('Value must be a number')

    def process_data(self):
        self.validate_input()
        # Simulate processing data
        result = {'processed_value': self.data['value'] * 2}
        return result

if __name__ == '__main__':
    input_data = json.loads('{"name": "example", "value": 10}')
    processor = DataProcessor(input_data)
    try:
        output = processor.process_data()
        print(json.dumps(output))
    except InputError as e:
        print(f'Input error: {e}')