a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if a > b and a > c:
    print("the greater number is"+str(a))
elif b > c and b > a:
    print("the greater number is" +str(b))
else :
    print("the greater number is" +str(c))
