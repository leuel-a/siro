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
