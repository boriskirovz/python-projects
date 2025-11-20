import string
import random

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols):
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()-_=+[]{};:,.?"


    if not characters:
        print("No character types selected. Exiting...")
        return None

    characters = "".join(random.choice(characters) for _ in range(length))
    return characters


if __name__ == "__main__":
    print("Password Generator")
    print("-" * 30)

    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_symbols = input("Include special characters? (y/n): ").lower() == "y"

    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)

    if password:
        print(f"\nGenerated password:{password}")