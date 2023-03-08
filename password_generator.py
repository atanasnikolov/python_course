from password_functions import weak_pass, mid_pass, strong_pass

lenght = 0

while True:
    user_password_choice = int(input("Select how strong should the password be from 1 to 3: "))
    if 0 < user_password_choice < 4:
        break


if user_password_choice == 1:
    print(weak_pass())
elif user_password_choice == 2:
    lenght = int(input("How long should the password be: "))
    print(mid_pass(lenght))
elif user_password_choice == 3:
    lenght = int(input("How long should the password be: "))
    print(strong_pass(lenght))
