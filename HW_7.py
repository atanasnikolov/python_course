number = int(input("Enter a number: "))

list_numbers = [11, 99, 1, 2, 39, 5, 8, 13, 21, 4, 55, 89]

list_smaller = [x for x in list_numbers if number > x]

print(list_smaller)

