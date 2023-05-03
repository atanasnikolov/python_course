#Exam 3
user_input = input('Enter your words: ')

ls = user_input.split(' ')

unique = set(ls)
resolution = []
for i in unique:
    resolution.append(i)

resolution.sort()
print(' '.join(resolution))

#Exam 4
class Rectangle:
    def __init__(self, a, b):
        self.sidea = a
        self.sideb = b
    
    def perimeter(self):
        perim = self.sidea * self.sideb
        return perim
    
pesho = Rectangle(3, 5)

print(pesho.perimeter())

#Exam 5
class American:
    name = ''
    
    def shoot(self):
        print("I can shoot")

class NewYorker(American):

    def display(self):
        print("My name is ", self.name)

Mikel = NewYorker()
 
Mikel.name = "Mikel"

 
Mikel.display()
Mikel.shoot()
        

#Exam 6
def zero_division():

    return 5 / 0

try:
    print(zero_division())
except ZeroDivisionError:
    print('You divided by zero')

#Exam 7
user_input = input('Please insert text here: ')

dict = {}

for i in user_input:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

print(dict)

#Exam 8
a = int(input('Provide a number: '))

b = str(a)
bb = str(b+b)
bbb = str(bb + b)
bbbb = str(bbb + b)

result = (int(b) + int(bb) + int(bbb) + int(bbbb))

print(result)

#Exam Bonus
passwords = input('Please input your password: ')


def check_low_letter(passwords):
    for i in passwords:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            return True
        else:
            continue
    return False

def check_cap_letter(passwords):
    for i in passwords:
        if i in 'ABCDEFGHIJKLMONPQRSTUVWXYZ':
            return True
        else:
            continue
    return False

def check_num(passwords): 
    for i in passwords:
        if i in '0123456789':
            return True
        else:
            continue
    return False

def check_symbol(passwords):
    for i in passwords:
        if i not in 'ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789':
            return True
        else:
            continue
    return False



low_letter = check_low_letter(passwords)
big_letter = check_cap_letter(passwords)
num = check_num(passwords)
symbol = check_symbol(passwords)

if 6 < len(passwords) < 21 and big_letter == low_letter == num == symbol == True:
    print('VALID PASSWORD')
else:
    print('INVALID PASSWORD')

print(big_letter)
print(low_letter)
print(num)
print(symbol)
