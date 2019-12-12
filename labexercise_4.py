#Write a function that returns the sum of multiples of 3 and 5 between 0
#and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6,
#9, 10, 12, 15, 18, 20
total_sum = 0
def sum_of_multiple():
 for number in range(start,end+1):
         if (i % 3 == 0 or i % 5 == 0):
             total_sum = total_sum + i
 print(number)

start = int(input("Enter the start limit:"))
end = int(input("Enter the end number:"))
i = int(input("The number to be multiplied:"))
sum_of_multiple()