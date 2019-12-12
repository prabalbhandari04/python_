#Accept string from the user and display only those characters which are
#present at an even index
def weird(str):
        result = ""
        for i in range(len(str)):
            if i % 2 == 0:
                result = result + str[i]
        return result
word = input("Enter a word : ")
print(weird(word))
