a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

#print(a, b, c)

list_numbers = [a, b, c]

x = a 
for i in list_numbers:
    if x < i:
        x = i

print(x)


"""
x = a
if x < b:
    x = b
elif x < c:
    x = c
else:
    x = a

print(x)
"""    
