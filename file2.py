import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = ''
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not any((use_uppercase, use_lowercase, use_digits, use_special)):
        raise ValueError("At least one character set must be selected.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Customizable Password Generator!")
    
    # Get desired password length from the user
    while True:
        try:
            length = int(input("Enter the length of the password you want to generate: "))
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")
            break
        except ValueError as ve:
            print(f"Error: {ve}")
    
    # Get user preferences for character sets
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print("\nGenerated Password:")
        print(password)
    except ValueError as ve:
        print(f"Error generating password: {ve}")

if __name__ == "__main__":
    main()
