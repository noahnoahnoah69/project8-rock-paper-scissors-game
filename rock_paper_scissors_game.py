import random

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print(f"Computer picked: {computer_pick}.")

    if user_input == computer_pick:
        print("Tie!")    
    
    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_win += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_win += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_win += 1

    else:
        print("You lost!")
        computer_win += 1

print(f"You won {user_win} times.")
print(f"Computer won {computer_win} times.")
print("Goodbye!")