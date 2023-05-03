# Напишете програма която играе “крави и бикове” с потребителя. Играта
# се играе така:
# Компютъра измисля случайно 4-цифрено число в което всички цифри
# са различни. От потребителя се иска да отгатне числото. За всяка
# позната цифра, която е на правилна позиция имаме “бик”. За всяка
# позната цифра, която не е на правилна позиция имаме “крава”. Всеки
# път когато потребителя се опитва да отгатне числото, програмата
# му казва колко “крави” и колко “бика” има. Играта свършва когато
# числото е отгатнато. На края на играта компютърът казва от колко
# опита потребителят е познал числото.
# Пример (измисленото число е 4271):
# Welcome to the Cows and Bulls Game!
# Guess a number: 1234
# 3
# 1 bull, 2 cows
# Guess a number: 1256
# 1 bull, 1 cow
# Guess a number: 4271
# Correct! It took you 3 turns

import random

counter = 0
sec_num = []
num_list = ['1','2','3','4','5','6','7','8','9','0']

while counter < 4:
    num = random.choice(num_list)
    if num in sec_num:
        continue
    else:
        sec_num.append(num)
    counter += 1

def num_check(list):
    if list[0] == '0':
        list[0], list[1] = list[1], list[0]
    return list

the_number = int(''.join(sec_num))

#print(num_check(sec_num))

user_input = input('Write a 4 digit number: ')
user_list = list(user_input)

print(user_list)