#Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.
#Hint: • a year is a leap year if its number is exactly divisible by 4 and is not
#exactly divisible by 100
#a year is always a leap year if its number is exactly divisible by 400
def leap_year():
    if year%4==0:
        print(year,"is a leap year")
    elif year%400==0:
        print(year, "is a leap year")
    else:
        print("It is not leap year")
year = int(input("Enter the year:"))
leap_year()
