# Напишете програма, която приема като аргумент число и казва дали
# даденото число е просто. (Просто число е число, което се дели без
# остатък само на 1 и на себе си.)


user_input1 = int(input('Type your num: '))

list = []
for num in range(1, user_input1 + 1):
    if user_input1 % num == 0:
        list.append(num)

dumb_list = [1, user_input1]
if list == dumb_list:
    print(f'{user_input1} is a dumb number')
else:
    print(f'{user_input1} is not a dumb number')