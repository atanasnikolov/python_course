# Напишете програма, която връща сумата от цифрите на положително
# число

user_input1 = input('Type your num: ')

sum = 0
for i in user_input1:
    sum += int(i)

print(sum)