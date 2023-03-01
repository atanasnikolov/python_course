number = input("Please enter a positive number: ")
list_number = list(number)
#print(list_number)

sum = 0

for i in range(len(list_number)):
    sum = sum + int(list_number[i])

print(sum)

