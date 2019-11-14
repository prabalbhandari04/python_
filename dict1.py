dict\
    ={"rollno":[1,2,3,4,5,6,7],"name":['ram','hari','shyam','ramey','acer','dell',"lenovo"],"marks":[80,83,94,89,73,92,87],"gender":["m","m","m","m","f","f","f"]}
for i in range(len(dict["rollno"])):
    if dict["gender"][i]=="m":
        print(dict["marks"][i])
        print(dict["name"])[i]

