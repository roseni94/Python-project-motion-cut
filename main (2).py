import random
import string

# Pre-defined lists of adjectives and nouns
adjectives = [
    "Cool", "Happy", "Funky", "Brave", "Shiny", "Lazy", "Smart", "Charming", "Bright", "Swift"
]
nouns = [
    "Tiger", "Dragon", "Phoenix", "Unicorn", "Panda", "Falcon", "Wolf", "Cheetah", "Eagle", "Llama"
]

def generate_username(include_numbers=True, include_special_chars=True, username_length=None):
    # Choose a random adjective and noun
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = f"{adj} {noun}"

    # Add numbers if selected
    if include_numbers:
        username += str(random.randint(1, 999))

    # Add special characters if selected
    if include_special_chars:
        username += random.choice(string.punctuation)

    # Adjust the length if specified
    if username_length:
        username = username[:username_length]

    return username

def save_to_file(usernames, filename="usernames.txt"):
    try:
        with open(filename, "a") as file:
            for username in usernames:
                file.write(username + "\n")
        print(f"Usernames saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    print("Welcome to the Random Username Generator!")
    usernames = []

    while True:
        # User preferences
        include_numbers = input("Include numbers in usernames? (yes/no): ").strip().lower() == "yes"
        include_special_chars = input("Include special characters in usernames? (yes/no): ").strip().lower() == "yes"
        username_length = input("Enter desired username length (or press Enter to skip): ").strip()

        try:
            username_length = int(username_length) if username_length else None
        except ValueError:
            print("Invalid length. Default length will be used.")
            username_length = None

        # Generate a username
        username = generate_username(include_numbers, include_special_chars, username_length)
        print(f"Generated Username: {username}")
        usernames.append(username)

        # Option to generate another username
        another = input("Generate another username? (yes/no): ").strip().lower()
        if another != "yes":
            break

    # Save usernames to file
    save_option = input("Do you want to save the generated usernames to a file? (yes/no): ").strip().lower()
    if save_option == "yes":
        save_to_file(usernames)

    print("Thank you for using the Random Username Generator!")

if __name__ == "__main__":
    main()
    