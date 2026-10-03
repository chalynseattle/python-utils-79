class DataError(Exception):
    """Base exception for data processing errors."""
    pass

class ValidationError(DataError):
    """Raised when data fails validation criteria."""
    pass

class ProcessingError(DataError):
    """Raised when data transformation fails."""
    def __init__(self, message, original_exception=None):
        super().__init__(message)
        self.original_exception = original_exception

class DataHandlerException(DataError):
    """Raised when handler state is invalid."""
    pass

def raise_if_invalid(data: dict, schema: list):
    """Validates that all required keys are present in data."""
    missing = [key for key in schema if key not in data]
    if missing:
        raise ValidationError(f"Missing required fields: {', '.join(missing)}")

def handle_data_failure(e: Exception):
    """Standard error wrapper for data operations."""
    if isinstance(e, DataError):
        return {"status": "error", "message": str(e)}
    return {"status": "critical", "message": "unexpected system failure"}