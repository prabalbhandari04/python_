# Write a Python function that accepts a string and calculate the number of
#upper case letters and lower case letters.
def count_upper_lower(string):
    lowercase_letter_count = 0
    uppercase_letter_count = 0

    for letter in string:
        if letter.isupper():
            uppercase_letter_count += 1
        elif letter.islower():
            lowercase_letter_count += 1

    print ("upper case letter:"+str(uppercase_letter_count)+" "+"lower case letter:"+ str(lowercase_letter_count))
word = str(input("Enter your word : "))
count_upper_lower(word)



