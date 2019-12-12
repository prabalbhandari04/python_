#Write a function called showNumbers that takes a parameter called limit. It
#should print all the numbers between 0 and limit with a label to identify the even and
#odd numbers. For example, if the limit is 3, it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
def show_numbers():
 for number in range(start, limit + 1):
    if number % 2 ==0 :
        print(number,"EVEN")
    else:
        print(number,"ODD")
number = int(input("Enter the number:"))
start = int(input("Enter the starting number:"))
limit =  int(input("Enter a number:"))
show_numbers()

