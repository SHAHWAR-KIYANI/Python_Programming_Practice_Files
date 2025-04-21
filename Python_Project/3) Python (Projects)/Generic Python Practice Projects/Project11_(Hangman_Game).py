import random

# Dictionary of words with hints
word_dict = {
    "python": "A popular programming language 🐍",
    "elephant": "A large mammal with a trunk 🐘",
    "guitar": "A musical instrument with strings 🎸",
    "chocolate": "A sweet made from cocoa 🍫",
    "laptop": "A portable computer 💻",
    "rocket": "Used to travel to space 🚀",
    "zebra": "A black and white striped animal 🦓",
    "banana": "A yellow fruit loved by monkeys 🍌",
    "diamond": "A precious stone 💎",
    "puzzle": "A game that tests your thinking skills 🧩"
}

# Cool Hangman Graphics
hangman_graphics = [
    """
      _______
     |       |
     |
     |
     |
     |
     |______
    """,
    """
      _______
     |       |
     |       O
     |
     |
     |
     |______
    """,
    """
      _______
     |       |
     |       O
     |       |
     |
     |
     |______
    """,
    """
      _______
     |       |
     |       O
     |    / |
     |
     |
     |______
    """,
    """
      _______
     |       |
     |       O
     |    / | \\
     |
     |
     |______
    """,
    """
      _______
     |       |
     |       O
     |    / | \\
     |     /
     |
     |______
    """,
    """
      _______
     |       |
     |       O   💀 GAME OVER! 💀
     |    / | \\
     |     /  \\
     |
     |______
    """
]


# Function to display game status
def display_status(word, guessed_letters, wrong_guesses, attempts):
    print("\n" + hangman_graphics[6 - attempts])  # Display current hangman stage
    displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(f"\n🔹 Word: {displayed_word}")
    print(f"❌ Wrong guesses: {', '.join(wrong_guesses) if wrong_guesses else 'None'}")
    print(f"❤️ Remaining attempts: {attempts}")


# Main Hangman function
def hangman():
    while True:
        word, hint = random.choice(list(word_dict.items()))  # Pick a random word and its hint
        word = word.lower()

        guessed_letters = []  # Track correctly guessed letters
        wrong_guesses = []  # Track incorrect guesses
        attempts = 6  # Number of attempts

        print("\n🎩 Welcome to the Ultimate Hangman! 🎭")
        print(f"💡 Hint: {hint}")
        print(hangman_graphics[0])  # Display starting graphic
        print("_ " * len(word))  # Display underscores for the word

        while attempts > 0:
            guess = input("\n🌠 Guess a letter: ").lower()  # Take user input

            if len(guess) != 1 or not guess.isalpha():
                print("⚠ Invalid input! Enter a single letter only.")
                continue  # Skip the rest of the loop

            if guess in guessed_letters or guess in wrong_guesses:
                print("🔁 You've already guessed that letter! Try a different one.")
                continue

            if guess in word:
                print(f"✅ Nice! '{guess}' is in the word!")
                guessed_letters.append(guess)
            else:
                print(f"❌ Oops! '{guess}' is not in the word.")
                wrong_guesses.append(guess)
                attempts -= 1

            display_status(word, guessed_letters, wrong_guesses, attempts)  # Update game status

            if "_" not in [letter if letter in guessed_letters else "_" for letter in word]:
                print("\n🎉🎊 CONGRATULATIONS! You guessed the word! 🎊🎉")
                break
        else:
            print("\n☠️ GAME OVER! The correct word was:", f"'{word.upper()}'")

        # Ask if the player wants to play again
        while True:
            play_again = input("\n🔄 Do you want to play again? (yes/y or no/n): ").strip().lower()
            if play_again in ["yes", "y"]:
                break  # Restart the game
            elif play_again in ["no", "n"]:
                print("\n👋 Thanks for playing! See you next time!")
                return  # Exit the game
            else:
                print("⚠ Invalid input! Please enter 'yes/y' or 'no/n'.")

# Run the game
if __name__ == "__main__":
    hangman()