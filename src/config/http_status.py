class HTTPStatus:
    """
    Common HTTP status codes for use in API responses.

    Each constant represents a standard HTTP response code with a brief
    description of when to use it.
    """

    OK = 200  # Success: Standard response for successful GET or general operations.
    CREATED = 201  # Created: Used after successfully creating a resource (e.g., POST).
    NO_CONTENT = 204  # No Content: Successful request with no response body (e.g., DELETE).

    BAD_REQUEST = 400  # Bad Request: Client sent invalid data or malformed request.
    UNAUTHORIZED = 401  # Unauthorized: Authentication is required or failed.
    FORBIDDEN = 403  # Forbidden: Authenticated but not allowed to access the resource.
    NOT_FOUND = 404  # Not Found: Resource doesn't exist or cannot be found.

    INTERNAL_SERVER_ERROR = 500  # Server Error: Generic server failure, not the client's fault.
