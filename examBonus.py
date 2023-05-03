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