# Напишете програма, която пита потребителя за число и извежда списък
# с делителите му.

user_input1 = int(input('Type your num: '))

for num in range(1, user_input1 + 1):
    if user_input1 % num == 0:
        print(num)