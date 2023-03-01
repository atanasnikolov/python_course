import random

rps = ["rock", "paper", "scissors"]
#pc_choice = random.choices(rps)

user_score = 0
pc_score = 0
draw = 0

print("Type \"Exit\" when you want to stop the game!")

while True:
    user_choice = input("Please select rock, paper or scissors: ")
    pc_choice = random.choice(rps)
    if user_choice == "exit" or user_choice == "Exit":
        break
    elif user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        print("Wrong input")
    elif user_choice == "rock" and str(pc_choice) == "scissors":
        print("YOU WIN")
        user_score += 1
    elif user_choice == "scissors" and str(pc_choice) == "paper":
        print("YOU WIN")
        user_score += 1
    elif user_choice == "paper" and str(pc_choice) == "rock":
        print("YOU WIN")
        user_score += 1
    elif user_choice == str(pc_choice):
        print("DRAW")
        draw += 1
    else:
        print("YOU LOST")
        pc_score += 1
        
print("WON: ", user_score, "\nDRAW: ", draw, "\nLOST :", pc_score)
    