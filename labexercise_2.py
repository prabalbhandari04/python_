#Write a function called fizz_buzz that takes a number.
#If the number is divisible by 3, it should return “Fizz”.
#If it is divisible by 5, it should return “Buzz”.
#If it is divisible by both 3 and 5, it should return “FizzBuzz”.
#Otherwise, it should return the same number.
def fizz_buzz():
    if number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    elif number%3==0 or number%5==0:
        print("FizzBuzz")
    else:
         print(number)
number = int(input("Enter a number:"))
fizz_buzz()