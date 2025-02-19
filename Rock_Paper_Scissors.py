#Task4 Rock_paper_scissors

import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

user_score = 0
computer_score = 0

while True:
    print("\nChoose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '4':
        print("Exiting the game. Goodbye!")
        break

    if choice == '1':
        user_choice = 'rock'
    elif choice == '2':
        user_choice = 'paper'
    elif choice == '3':
        user_choice = 'scissors'
    else:
        print("Invalid input. Please enter 1, 2, 3, or 4.")
        continue

    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = get_winner(user_choice, computer_choice)
    print(result)

    if "win" in result:
        user_score += 1
    elif "lose" in result:
        computer_score += 1

    print(f"User Score: {user_score} | Computer Score: {computer_score}")
