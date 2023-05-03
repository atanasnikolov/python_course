# Напишете програма, която пита потребителя за число и извежда
# съобщение дали числото е четно или нечетно.
# Пример:
# Enter a number: 9
# 9 in an odd number

user_input1 = int(input('Type your num: '))

if user_input1 % 2 == 0:
    print(f'{user_input1} is an even number')
else:
    print(f'{user_input1} is an odd number')