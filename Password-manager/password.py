import secrets
import string


# ---------------- PASSWORD GENERATOR ----------------
def generate_password(length, use_upper, use_lower, use_numbers, use_symbols):
    """
    Generate a secure random password.
    """

    try:
        if not isinstance(length, int):
            raise TypeError("Password length must be an integer.")

        if length < 4:
            raise ValueError("Password length must be at least 4 characters.")

        char_pool = ""

        if use_upper:
            char_pool += string.ascii_uppercase

        if use_lower:
            char_pool += string.ascii_lowercase

        if use_numbers:
            char_pool += string.digits

        if use_symbols:
            char_pool += string.punctuation

        if not char_pool:
            raise ValueError("Select at least one character type.")

        password = "".join(
            secrets.choice(char_pool)
            for _ in range(length)
        )

        return password

    except Exception as e:
        print(f"Password Generation Error: {e}")
        return None


# ---------------- PASSWORD STRENGTH ----------------
def check_strength(password):
    """
    Returns:
        Weak
        Medium
        Strong
    """

    try:
        if not password:
            return "Weak"

        score = 0

        if len(password) >= 8:
            score += 1

        if any(c.isupper() for c in password):
            score += 1

        if any(c.islower() for c in password):
            score += 1

        if any(c.isdigit() for c in password):
            score += 1

        if any(c in string.punctuation for c in password):
            score += 1

        if len(password) >= 12:
            score += 1

        if score <= 2:
            return "Weak"

        elif score <= 4:
            return "Medium"

        else:
            return "Strong"

    except Exception as e:
        print(f"Password Strength Error: {e}")
        return "Weak"
