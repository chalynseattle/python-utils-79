import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(max_attempts=3, delay=1.0, exceptions=(Exception,)): 
    """Decorator to retry a function if it raises specified exceptions."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Final attempt {attempts} failed for {func.__name__}")
                        raise
                    
                    logger.warning(f"Attempt {attempts} failed, retrying in {delay}s: {e}")
                    time.sleep(delay)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def fetch_with_retry(func, *args, **kwargs):
    """Functional wrapper for network-bound operations with retry logic."""
    retry_logic = retry(max_attempts=3, delay=2.0)(func)
    return retry_logic(*args, **kwargs)