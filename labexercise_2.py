#Write a Python program to convert temperatures to and from celsius,
#fahrenheit.
 #C = (5/9) * (F - 32)

def temperature():
    C = int((5 / 9) * (F - 32))
    print("The weather is "+ " " + str(C) + " "+ "degree celsuis.")
F = int(input("Enter the temperature in Fahrenheit : "))
temperature()