s = "| | | |"
user_input = input("what to swap A B C? ")

def swap_place(column, row, symbol):
    ls = list(row)

    if column == "A":
        ls[1] = symbol
    elif column == "B":
        ls[3] = symbol
    elif column == "C":
        ls[5] = symbol

    row = ''.join(ls)
    return row

print(swap_place(user_input[0], s, "O"))

"""
ls[1] = 
ls[3] = 
ls[5] = 
s = ''.join(ls)
print(s)
print(s[3])
"""
