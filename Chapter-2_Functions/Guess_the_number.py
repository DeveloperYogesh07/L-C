import random

def is_valid_guess(guess):
    """Check if the input guess is a valid number between 1 and 100."""
    return guess.isdigit() and 1 <= int(guess) <= 100

def get_guess():
    """Prompt the user to guess a number and return their input."""
    return input("Guess a number between 1 and 100: ")

def provide_feedback(secret_number, guess_count):
    """Provide feedback on the number of guesses the user took."""
    print(f"Congratulations! You guessed the number in {guess_count} guesses!")

def guess_the_number():
    """Main function to handle the guessing game logic."""
    secret_number = random.randint(1, 100)
    guess_count = 0
    guessed_correctly = False

    while not guessed_correctly:
        guess = get_guess()

        if not is_valid_guess(guess):
            print("Invalid input. Please enter a number between 1 and 100.")
            continue

        guess_count += 1
        guess = int(guess)

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            provide_feedback(secret_number, guess_count)
            guessed_correctly = True

# Start the game
guess_the_number()
