import random

def play_game():
    number = random.randint(1, 100)
    attempts = 10

    print("Guess the number between 1 and 100. You have 10 attempts!")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You guessed it right!")
            break

        attempts -= 1
        print(f"Attempts left: {attempts}")

    if attempts == 0:
        print("You lost. Want to play again? ")
        retry = input("Type 'Y', 'YES', 'y', 'yes', or 'ok' to play again: ")
        if retry in ['Y', 'YES', 'y', 'yes', 'ok']:
            play_game()
        else:
            print("Thanks for playing!")

play_game()
