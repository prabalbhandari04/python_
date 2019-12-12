#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

#defining a function that returns zero if two values asked from the user is same
def sum(a, b, c):
    if a == b or b == c or a == c:
        sum = 0
    else:
        sum = a + b + c
    return sum
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
print(sum(a,b,c))