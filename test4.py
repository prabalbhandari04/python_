a = float(input("enter number"))
b = float(input("enter number"))
c = float(input("enter number"))
d = float(input("enter number"))
e = float(input("enter number"))
f=(a+b+c+d+e)
g=f/5
if g >= 90:
    print("A+")
elif g >= 80:
    print("A")
elif g >= 70:
    print("B")
elif g >= 60:
    print("C")
elif g >= 50:
    print("D")
else:
    print("failed")