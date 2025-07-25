import bcrypt

def hash_password(password: str) -> str:
    """Hashes a password

    :param password: the password to be hashed

    :rtype: str
    :return: the hashed password
    """
    salt_rounds = bcrypt.gensalt(10)
    hashed_password = bcrypt.hashpw(password.encode(), salt_rounds)
    return hashed_password.decode()


def check_password(candidate_passwd: str, hashed_passwd: str) -> bool:
    """Check the password against a candidate password

    :param candidate_passwd: the candidate password
    :param hashed_passwd: the hashed password

    :rtype: bool
    """
    return bcrypt.checkpw(candidate_passwd.encode(), hashed_passwd.encode())


def info(msg: str):
    """
    Prints an informational message to the console, prefixed with a bold, blue `[INFO]`.

    This function is typically used for general-purpose logging or providing status updates
    that are not critical but helpful for understanding the application's flow.

    :param msg: The message string to display.

    Usage:
     >>> info("The application has started successfully.")
     [INFO] The application has started successfully.
    """
    print(f"\033[1;34m[INFO]\033[0m {msg}")  # Bold Blue


def success(msg: str):
    """
    Prints a success message to the console, prefixed with a bold, green `[SUCCESS]`.

    This is best used to indicate that a specific operation or task has completed
    without any issues.

    :param msg: The message string to display.

    Usage:
     >>> success("Database connection established.")
     [SUCCESS] Database connection established.
    """
    print(f"\033[1;32m[SUCCESS]\033[0m {msg}")  # Bold Green


def warning(msg: str):
    """
    Prints a warning message to the console, prefixed with a bold, yellow `[WARNING]`.

    Use this function to highlight potential issues that do not prevent the application
    from running but may require attention, such as a deprecated feature being used.

    :param msg: The message string to display.

    Usage:
     >>> warning("The API version you are using is deprecated and will be removed soon.")
     [WARNING] The API version you are using is deprecated and will be removed soon.
    """
    print(f"\033[1;33m[WARNING]\033[0m {msg}")  # Bold Yellow


def error(msg: str):
    """
    Prints an error message to the console, prefixed with a bold, red `[ERROR]`.

    This should be used to report critical errors or failures that prevent a specific
    operation from completing or disrupt the normal flow of the application.

    :param msg: The message string to display.

    Usage:
     >>> error("Failed to connect to the server.")
     [ERROR] Failed to connect to the server.
    """
    print(f"\03f[1;31m[ERROR]\033[0m {msg}")  # Bold Red

