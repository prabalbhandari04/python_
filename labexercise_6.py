#Write a Python program to count the number of even and odd numbers from a
#series of numbers.
number = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
even_count = 0
odd_count = 0
for i in number:
     if i%2==0:
        even_count += 1
     else:
        odd_count += 1

print ("Even number : "+str(even_count)+ " " +"odd number : "+ str(odd_count))
