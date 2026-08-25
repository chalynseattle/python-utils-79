import time
import random
from functools import wraps

def retry(max_attempts=3, delay=1.0, backoff_factor=2.0, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            current_delay = delay
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    attempt += 1
                    if attempt == max_attempts:
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff_factor
                    current_delay += random.uniform(0, 0.5)
            return None
        return wrapper
    return decorator

class NetworkHandler:
    def __init__(self, base_url):
        self.base_url = base_url

    @retry(max_attempts=4, delay=0.5, exceptions=(ConnectionError, TimeoutError))
    def get_resource(self, endpoint):
        if random.random() < 0.7:
            raise ConnectionError("Network failure")
        return f"Data from {self.base_url}{endpoint}"

    @retry(max_attempts=3, delay=1.0)
    def post_data(self, endpoint, data):
        if random.random() < 0.5:
            raise TimeoutError("Request timed out")
        return f"Posted to {endpoint}: {data}"

if __name__ == "__main__":
    handler = NetworkHandler("https://api.example.com")
    try:
        result = handler.get_resource("/users")
        print(result)
    except Exception as e:
        print(f"Failed after retries: {e}")