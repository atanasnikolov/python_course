year = int(input("Enter a year: "))

if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
    print("The year is leap!")
else:
    print("The year is not leap")
    
print("Done!")