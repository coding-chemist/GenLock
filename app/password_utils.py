import random
import string
import re

def generate_password(length=16, include_special=True, enforce_rules=True):
    """
    Generate a strong password based on defined rules.
    - At least one uppercase, one lowercase, one digit, and one special character if rules are enforced.
    - Avoids continuous sequences of 3-4 alphabetic characters unless mixed case.
    """
    if length < 12:  # Minimum recommended length
        raise ValueError("Password length should be at least 12 characters for security.")

    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    all_chars = lowercase + uppercase + digits + special

    password = []

    # Ensure enforced rules if required
    if enforce_rules:
        password.append(random.choice(lowercase))
        password.append(random.choice(uppercase))
        password.append(random.choice(digits))
        if include_special:
            password.append(random.choice(special))

    # Fill the rest of the password
    while len(password) < length:
        char = random.choice(all_chars)
        if is_valid_char_to_add(password, char):
            password.append(char)

    random.shuffle(password)  # Shuffle for randomness
    return ''.join(password)


def is_valid_char_to_add(password, char):
    """
    Check if the character can be added to the password:
    - Prevent sequences of 3+ alphabetic characters of the same case.
    """
    if not password:
        return True

    # Check last three characters
    last_chars = password[-3:] if len(password) >= 3 else password

    # If char is alphabetic, check sequence rules
    if char.isalpha():
        sequence = last_chars + [char]
        if len(sequence) >= 3:
            # Check for all upper or all lower sequences
            if all(c.islower() for c in sequence) or all(c.isupper() for c in sequence):
                return False
    return True


def check_password_security(password):
    """
    Evaluate the strength of a password based on its characteristics.
    """
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    # Detect consecutive same-case alphabets
    consecutive_alpha_pattern = r'([a-z]{3,}|[A-Z]{3,})'
    has_consecutive_alpha = bool(re.search(consecutive_alpha_pattern, password))

    # Detect consecutive same digits
    consecutive_digit_pattern = r'(\d)\1{2,}'  # e.g., "111"
    has_consecutive_digits = bool(re.search(consecutive_digit_pattern, password))

    # Check if the password is too simple
    weak_patterns = ["password", "qwerty", "123", "abc", "letmein"]
    is_simple = any(pattern in password.lower() for pattern in weak_patterns)

    # Base conditions for "Very Weak"
    if length < 8 or is_simple or password.isdigit() or password.isalpha():
        return "Very Weak"

    # Apply additional deductions based on consecutive patterns
    if has_consecutive_alpha or has_consecutive_digits:
        return "Weak"

    # Scoring for remaining passwords
    score = 0
    if length >= 12:  # Strong length
        score += 2
    elif length >= 8:  # Moderate length
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    # Assign levels based on the score
    levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    return levels[min(score, len(levels) - 1)]