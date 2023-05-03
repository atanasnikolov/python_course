# Напишете програма, която приема име и възраст от потребителя и
# принитира през коя година потребителят ще стане на 100 години.
# Пример:
# Enter your name: Evgeni
# Enter your age: 41
# Evgeni will be 100 years old in the year 2078.

user_input = (input('Type your name: '))
age_input = int(input('Type your age: '))

born_year = 2023 - age_input
year_100 = born_year + 100

print(f'{user_input}  will be 100 years old in the year {year_100}')