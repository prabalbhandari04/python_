# Write a Python function that takes a number as a parameter and check the
#number is prime or not.
def prime_or_not():
    num = int(input("enter a number: "))

    for i in range(2, num):
        if num % i == 0:
            print("not prime number")
            break
    else:
        print("prime number")
prime_or_not()