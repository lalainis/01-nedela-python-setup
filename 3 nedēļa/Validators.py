def is_valid_email(email: str) -> bool:
    """
    Checks if the email address is valid.
    Args:
        email (str): The email address to validate.
    Returns:
        bool: True if valid, False otherwise.
    """
    if "@" in email and "." in email.split("@")[-1]:
        return True
    return False

def is_valid_phone_number(phone: str) -> bool:
    """
    Checks if the phone number is valid (8 digits).
    Args:
        phone (str): The phone number to validate.
    Returns:
        bool: True if valid, False otherwise.
    """
    if phone.isdigit() and len(phone) == 8:
        return True
    return False
def is_valid_lv_phone_number(phone: str) -> bool:
    """
    Checks if the phone number is a valid Latvian number (must start with +371 or 00371 and have exactly 8 digits after the code).
    Args:
        phone (str): The phone number to validate.
    Returns:
        bool: True if valid, False otherwise.
    Example:
        >>> is_valid_lv_phone_number('+37112345678')
        True
        >>> is_valid_lv_phone_number('0037112345678')
        True
        >>> is_valid_lv_phone_number('12345678')
        False
    """
    if not isinstance(phone, str):
        return False
    if phone.startswith('+371'):
        rest = phone[4:]
        return len(rest) == 8 and rest.isdigit()
    if phone.startswith('00371'):
        rest = phone[5:]
        return len(rest) == 8 and rest.isdigit()
    return False

def is_valid_age(age: int) -> bool:
    """
    Checks if the age is valid (0-150).
    Args:
        age (int): The age to validate.
    Returns:
        bool: True if valid, False otherwise.
    """
    if not isinstance(age, int):
        return False
    if 0 <= age <= 150:
        return True
    return False

def is_strong_password(password: str) -> bool:
    """
    Checks if the password is strong (at least 8 characters, upper and lower case letters, digits).
    Args:
        password (str): The password to validate.
    Returns:
        bool: True if strong, False otherwise.
    """
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit

def is_valid_date(date_str: str) -> bool:
    """
    Checks if the date is valid (format DD-MM-YYYY).
    Args:
        date_str (str): The date string to validate.
    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        day, month, year = map(int, date_str.split('-'))
        if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
            return True
    except ValueError:
        return False
    return False

if __name__ == "__main__":
    # Test email validation
    print("Email valid (test@example.com):", is_valid_email("test@example.com"))
    print("Email valid (invalid):", is_valid_email("invalid"))

    # Test phone validation (8 digits)
    print("Phone valid (12345678):", is_valid_phone_number("12345678"))
    print("Phone valid (1234):", is_valid_phone_number("1234"))

    # Test Latvian phone validation
    print("LV phone valid (+37112345678):", is_valid_lv_phone_number("+37112345678"))
    print("LV phone valid (0037112345678):", is_valid_lv_phone_number("0037112345678"))
    print("LV phone valid (12345678):", is_valid_lv_phone_number("12345678"))
    print("LV phone valid (+3711234567):", is_valid_lv_phone_number("+3711234567"))

    # Test age validation
    print("Age valid (25):", is_valid_age(25))
    print("Age valid (200):", is_valid_age(200))
    print("Age valid ('abc'):", is_valid_age('abc'))

    # Test strong password
    print("Strong password (Abcdef12):", is_strong_password("Abcdef12"))
    print("Strong password (abcdef12):", is_strong_password("abcdef12"))
    print("Strong password (ABCDEF12):", is_strong_password("ABCDEF12"))
    print("Strong password (Abcdefgh):", is_strong_password("Abcdefgh"))

    # Test date validation
    print("Date valid (01-01-2000):", is_valid_date("01-01-2000"))
    print("Date valid (31-02-2000):", is_valid_date("31-02-2000"))
    print("Date valid (bad):", is_valid_date("bad"))
