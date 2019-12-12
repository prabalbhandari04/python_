#Write a program to find the factorial of a number.
def factorial(i):
    if i==0:
        return 1
    else:
        return i*factorial(i-1)
i = int(input("Enter a number: "))
print(factorial(i))