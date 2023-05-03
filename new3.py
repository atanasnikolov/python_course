# Напишете програма, която намира най-голямото от три числа въведени
# от потребителя, без да ползвате вградената функция max.


user_input1 = int(input('Type your num1: '))
user_input2 = int(input('Type your num2: '))
user_input3 = int(input('Type your num3: '))

max_num = 0

list = [user_input1, user_input2, user_input3]

for num in list:
    if max_num < num:
        max_num = num
print(max_num)