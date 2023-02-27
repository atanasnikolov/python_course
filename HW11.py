import random


computer_number = random.randint(1, 9)
i = 1
print("You can exit the program by typing 'exit'")
while True:
    user_number = (input("Please select a number between 1-9: "))
    if user_number == "exit" or user_number == "Exit":
        print("Exiting program")
        i -= 1
        break
    elif int(user_number) < 1 or int(user_number) > 9:
        print("Number not in range!")
    elif int(user_number) > computer_number:
        print("Pick a lower number!")
    elif int(user_number) < computer_number:
        print("Pick a higher number")
    elif int(user_number) == computer_number:
        print("You guessed it!")
        break
    i += 1

print("Number of attempts: ", i)