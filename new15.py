# Напишете програма, която генерира два случайни списъка с числа,
# например:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# и извежда на екрана само тези числа които са общи и за двата списъка
# (без повторения). Например за горните два списъка това са:
# [1, 2, 3, 5, 8, 13]

import random
i = 0
a = []
b = []
lenght = random.randint(0, 9)
while i < lenght:
    a.append(random.randrange(10))
    b.append(random.randrange(10))
    i += 1
    if i > lenght:
        break

sum = []
for n in a:
    if n in b:
        sum.append(n)

sumset = set(sum)
empty = []
for i in sumset:
    empty.append(i)


print(empty)