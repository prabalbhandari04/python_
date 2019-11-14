a=float(input("enter number"))
b=float(input("enter number"))
c=float(input("enter number"))
if a > b and a > c:
    temp=a
elif b > c and b > a:
    temp=b
else :
    temp=c
    print("greater number is",temp)

                