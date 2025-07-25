from enum import Enum

class AppEnum(Enum):
    """An enumeration of the application errors."""
    RESOURCE_NOT_FOUND = 1
    INVALID_INPUT = 2
    AUTHENTICATION_FAILED = 3
    INVALID_EMAIL_OR_PASSWORD = 4


class AppError(Exception):
    """
    Global application error.

    :param enum: The AppEnum member associated with the error.
    :param message: A specific, optional error message.
    """
    def __init__(self, enum: AppEnum, message: str = ''):
        super().__init__(message or enum.name)
        self.enum = enum
        self.message = message


    def __str__(self):
        if self.message:
            return f"[{self.enum.name}]: {self.message}"
        return f"An error occurred: {self.enum.name}"

