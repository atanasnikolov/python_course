# Напишете програма, която пита потребителя за число и извежда списък
# с всички числа измежду [11, 99, 1, 2, 39, 5, 8, 13, 21, 4, 55, 89], които са
# по-малки от въведеното от портребителя число.

list = [11, 99, 1, 2, 39, 5, 8, 13, 21, 4, 55, 89]
result = []
user_input1 = int(input('Type your num: '))

for num in list:
    if user_input1 > num:
        result.append(num)

print(result)