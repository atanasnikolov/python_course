# Напишете функция, която приема подреден списък от числа (подредени
# от най-малкото към най-голямото) и още едно число. Функцията трябва
# да връща True или False в зависимост от това дали числото е в списъка
# ли не.
# Екстра: Използвайте “binary search”.


list = [1,123,123,5,5,325,23,3123,5,56,123,6,123]
num = 0
def check(list, num):
    for i in list:
        if i == num:
            return True
        else:
            continue
    return False

print(check(list, num))