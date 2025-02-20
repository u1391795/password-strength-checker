import re

def main():
    """Main function to prompt user input and check password strength."""
    print("Welcome to Password Strength Checker")
    password = input("Enter a password to check: ")
    
    strength, tips = check_password_strength(password)
    print("\n" + strength)
    
    if tips:
        for tip in tips:
            print(f"- {tip}")

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters).")

    # Character variety checks
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r'[\W_]', password):  # Checks for special characters
        score += 1
    else:
        feedback.append("Include at least one special character (e.g., !@#$%).")

    common_passwords = [
    "password", "123456", "123456789", "qwerty", "12345", "1234", "111111", "12345678",
    "abc123", "password1", "123123", "admin", "letmein", "welcome",
    "iloveyou", "batman", "hello", "whatever", "qazwsx", "login", "starwars",
    "654321", "123321", "123", "google", "password123", "123qwe", "zaq12wsx", "qwerty123",
    "qwert", "1q2w3e4r", "1qaz2wsx", "zxcvbn", "asdfgh", "qwertyuiop", "P@ssw0rd",
    "Passw0rd", "qwerty1", "Mypass123", "letmein123", "Pa$$w0rd",
    "Welcome123", "changeme", "newpass", "loveme", "letmein!", "iloveyou!", "password!", "password123!", "hello123"
    ]
    if password.lower() in common_passwords:
        score = 0
        feedback.append("Your password is too common. Choose something more unique.")

    # Strength rating
    if score >= 5:
        return "Strong password:", feedback
    elif score >= 3:
        return "Moderate password:", feedback
    else:
        return "Weak password:", feedback

