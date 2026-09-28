from typing import Any, Callable, Dict, Optional

class RequestHandler:
    """Handles incoming request data and dispatching."""

    def __init__(self, routes: Dict[str, Callable[[Any], Any]]) -> None:
        self._routes: Dict[str, Callable[[Any], Any]] = routes

    def handle(self, path: str, data: Any) -> Optional[Any]:
        """
        Dispatches request to appropriate route handler.

        Args:
            path: URL path to match.
            data: Data payload to process.

        Returns:
            Processed response or None if no route found.
        """
        handler = self._routes.get(path)
        if handler:
            return handler(data)
        return None

def create_response(status: int, body: str) -> Dict[str, Any]:
    """
    Formats response structure for client return.

    Args:
        status: HTTP status code.
        body: Content string.

    Returns:
        Dictionary containing status and body.
    """
    return {"status": status, "body": body}

if __name__ == "__main__":
    routes = {"/ping": lambda x: "pong"}
    handler = RequestHandler(routes)
    print(handler.handle("/ping", None))