#WAP which accepts marks of four subjects and display total marks, percentage and grade.
#Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass,
#less than 40% –> fail
english = float(input("Enter the mark:"))
math  = float(input("Enter the mark:"))
science  = float(input("Enter the mark:"))
computer  = float(input("Enter the mark:"))
total_marks = english+math+science+computer
percentage= total_marks/4
print("The total marks is",total_marks)
print("The percentage is ",percentage)
if percentage>=70:
    print("Distinction")
elif percentage>=60:
    print("First")
elif percentage>=40:
    print("pass")
else:
    print("fail")




