# Напишете програма, която генерира случайни, трудни за отгатване
# пароли. Трудните за отгатване пароли обикновено съдържат малки
# и големи букви, числа и препинателни знаци. Програмата трябва да
# генерира всеки път различни пароли.
# Екстра: Направете програмата да пита потребителя колко “силна”
# иска да е генерираната парола, и съответно да генерира по-дълга или
# по-къса парола. Най-слабите пароли може избирате от предварително
# зададен списък от думи.
import random
 
list = [1,2,3,4,5,6,7,8,9]
list2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list3 = [x.upper() for x in list2]
list4 = ['!','@','#','$','%','^','&','*','_','+','<','>','?']

list_list = [list, list2, list3, list4]

user_input1 = int(input('Lenght of pass: '))
password = []



while True:
    pass_lists = random.choice(list_list)
    pass_element = random.choice(pass_lists)
    password.append(pass_element)
    user_input1 -= 1
    if user_input1 < 1:
        break

print(''.join(str(e) for e in password))
 