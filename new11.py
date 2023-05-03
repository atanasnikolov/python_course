# Напишете програма, която генерира случайно число от 1 до 9 иска
# от потребителя да отгатне числото, като всеки път му казва му казва
# “по-голямо,”по-малко"или “точно”.
# Екстри:
# • Играта да спира когато потребителя въведе “exit”.
# • Когато потребителят познае числото, да се извежда броя на
# опитите, които е направил.
import random
random_num = random.randint(1,9)

num_tries = 0

while True:
    user_input1 = int(input('Type your num: '))
    num_tries += 1
    if user_input1 < random_num:
        print('The number is higher!')
    elif user_input1 > random_num:
        print('The number is lower!')
    elif user_input1 == random_num:
        print(f'The is the correct number. You guessed it on your {num_tries} try!')
