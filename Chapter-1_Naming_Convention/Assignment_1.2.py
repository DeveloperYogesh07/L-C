# program is to guess the correct number between 1 to 100

import random

def is_valid_guess(guess):
    """Checks if the guess is a valid number between 1 and 100."""
    if guess.isdigit() and 1 <= int(guess) <= 100:
        return True
    else:
        return False

def main():
    """Main function to play the number guessing game."""
    secret_number = random.randint(1, 100)
    guessed_correctly = False
    attempts = 0

    user_guess = input("Guess a number between 1 and 100: ")

    while not guessed_correctly:
        if not is_valid_guess(user_guess):
            user_guess = input("Invalid input. Please enter a number between 1 and 100: ")
            continue
        else:
            attempts += 1
            user_guess = int(user_guess)

        if user_guess < secret_number:
            user_guess = input("Too low. Guess again: ")
        elif user_guess > secret_number:
            user_guess = input("Too high. Guess again: ")
        else:
            print(f"Congratulations! You guessed the secret number in {attempts} attempts!")
            guessed_correctly = True

if __name__ == "__main__":
    main()
