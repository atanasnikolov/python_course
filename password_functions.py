import random

weak_passwords = ["mypass", "dogname", "favoritefood", "thisisabadpass", "mybirthdaydate"]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
big_letters = [x.upper() for x in letters]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '=', '+']

list_of_lists = [letters, numbers, symbols, big_letters]
list_select = random.choice(list_of_lists)
char_select = random.choice(list_select)

def weak_pass():
    return random.choice(weak_passwords)

#print(weak_pass())

def mid_pass(lenght = 5):
    i = 0
    password = []
    while i <= lenght:
        list_of_lists = [letters, numbers, big_letters]
        list_select = random.choice(list_of_lists)
        char_select = random.choice(list_select)
        password.append(char_select)
        i += 1
    return ''.join(password)

#print(mid_pass())

def strong_pass(lenght = 8):
    i = 0
    password = []
    while i <= lenght:
        list_of_lists = [letters, numbers, symbols, big_letters]
        list_select = random.choice(list_of_lists)
        char_select = random.choice(list_select)
        password.append(char_select)
        i += 1
    return ''.join(password)

#print(strong_pass())

# lenght = 0
#  
# while True:
#      user_password_choice = int(input("Select how strong should the password be from 1 to 3: "))
#      if 0 < user_password_choice < 4:
#          break
#  
#  
# if user_password_choice == 1:
#      print(weak_pass())
# elif user_password_choice == 2:
#      lenght = int(input("How long should the password be: "))
#      print(mid_pass(lenght))
# else:
#      lenght = int(input("How long should the password be: "))
#      print(strong_pass(lenght))
