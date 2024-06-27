import string

def evaluate_password_strength(password):
    # Criteria variables
    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if length_ok and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length_ok and has_upper and has_lower and has_digit:
        return "Moderate"
    else:
        return "Weak"

password = input("Enter your password: ")
strength = evaluate_password_strength(password)
print(f"The strength of your password '{password}' is: {strength}")
