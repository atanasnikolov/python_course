# Напишете програма, която принтира таблицата за умножение (от едно
# до девет) за число, въведено от потребителя.

user_input1 = int(input('Type your num: '))

for i in range (10):
    multi = i * user_input1
    print(f'{user_input1} X {i} = {multi}' )