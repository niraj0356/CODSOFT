import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (computer_choice == 'rock' and user_choice == 'scissors') or \
         (computer_choice == 'scissors' and user_choice == 'paper') or \
         (computer_choice == 'paper' and user_choice == 'rock'):
        return "You lose!"
    else:
        return "You win!"

print(rock_paper_scissors())
