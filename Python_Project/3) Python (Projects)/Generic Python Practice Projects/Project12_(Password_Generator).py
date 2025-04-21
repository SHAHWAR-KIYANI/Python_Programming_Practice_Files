import random
import string

def display_header():
    print("=" * 60)
    print("\t\tPassword Generator")
    print("=" * 60)

def evaluate_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length >= 12 and score == 4:
        return "\U0001F7E2 Strong"
    elif length >= 8 and score >= 3:
        return "\U0001F7E1 Medium"
    else:
        return "\U0001F534 Weak"

def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    char_sets = []
    if use_lower:
        char_sets.append(string.ascii_lowercase)
    if use_upper:
        char_sets.append(string.ascii_uppercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_symbols:
        char_sets.append(string.punctuation)

    if not char_sets:
        print("Error: No character set selected!")
        return None

    # Ensure at least one character from each selected category
    if len(char_sets) > length:
        print("Error: Selected character types exceed password length. Reduce selection or increase length.")
        return None

    password = [random.choice(char_set) for char_set in char_sets]
    all_chars = ''.join(char_sets)
    password += [random.choice(all_chars) for _ in range(length - len(password))]
    random.shuffle(password)

    return "".join(password)

def main():
    while True:
        display_header()

        try:
            password_length = int(input("Enter the password length: "))
            if password_length <= 0:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        while True:
            use_lower = input("Include lowercase letters? (yes/y or no/n): ").strip().lower() in ('yes', 'y')
            use_upper = input("Include uppercase letters? (yes/y or no/n): ").strip().lower() in ('yes', 'y')
            use_digits = input("Include digits? (yes/y or no/n): ").strip().lower() in ('yes', 'y')
            use_symbols = input("Include special characters? (yes/y or no/n): ").strip().lower() in ('yes', 'y')

            selected_types = sum([use_lower, use_upper, use_digits, use_symbols])
            if selected_types > password_length:
                print("Error: The number of selected character types exceeds the password length. Please try again.")
            else:
                break

        print()
        output = generate_password(password_length, use_lower, use_upper, use_digits, use_symbols)
        if output:
            print("_" * (password_length + 30))
            print(f"Generated Password: {output}")
            print("_" * (password_length + 30))
            print(f"Password Strength: {evaluate_strength(output)}")
        print()

        run_again = input("Do you want to generate another password? (yes/y or no/n): ").strip().lower()
        if run_again not in ('yes', 'y'):
            print("Exiting the Advanced Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()