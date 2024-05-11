import random


def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number game!")

    while True:
        try:
            # Prompt the user to input their guess
            user_guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            # Check if the guess is correct
            if user_guess == number_to_guess:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
                print(f"It took you {attempts} attempts to win the game.")
                break
            # If the guess is too high
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            # If the guess is too low
            else:
                print("Too low! Try again.")
        except ValueError:
            print("Please enter a valid number.")


# Call the function to start the game
guess_the_number()
