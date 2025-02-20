import re

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

    # Common password check (simple example)
    common_passwords = ["password", "123456", "qwerty", "letmein", "abc123"]
    if password.lower() in common_passwords:
        score = 0
        feedback.append("Your password is too common. Choose something more unique.")

    # Strength rating
    if score >= 5:
        return "Strong password 💪", feedback
    elif score >= 3:
        return "Moderate password 😐", feedback
    else:
        return "Weak password ⚠️", feedback

# Example usage
password = input("Enter a password to check: ")
strength, tips = check_password_strength(password)
print(strength)
for tip in tips:
    print(f"- {tip}")
