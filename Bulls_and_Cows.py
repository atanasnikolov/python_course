import random

pc_choice = random.randint(1000,10000)
list_pc = [int(x) for x in pc_choice]
print(list_pc)
i = 0
print(a)
while True:
    user_choice = int(input("Select a 4 digit number: "))
    if pc_choice == user_choice:
        print("You win! It took you ", i, " tries")

    
    i += 1