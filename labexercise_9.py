# Write a Python function that checks whether a passed string is palindrome or
#not.
def palindrome():
    reverse = word[::-1]
    if reverse==word:
        print("palindrome")
    else:
        print("not palindrome")
word = str(input("Enter a word:"))
palindrome()