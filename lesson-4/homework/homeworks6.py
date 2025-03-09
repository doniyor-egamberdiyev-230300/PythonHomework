# Prime Numbers between 1 and 100
print("Prime numbers between 1 and 100:")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

print("\n\nRock, Paper, Scissors Game")
import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while player_score < 5 and computer_score < 5:
    computer_choice = random.choice(choices)
    player_choice = input("Enter rock, paper, or scissors: ").lower()

    if player_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "scissors" and computer_choice == "paper") or \
            (player_choice == "paper" and computer_choice == "rock"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score - You: {player_score}, Computer: {computer_score}\n")

if player_score == 5:
    print("Congratulations! You won the match!")
else:
    print("Computer wins the match. Better luck next time!")
