dict = {'roll': [1, 2, 3, 4, 5],'name':['a', 'b', 'c', 'd', 'e']}
roll=dict['roll']
name=dict['name']
data=input("enter your roll no:")
for i in range(len(roll)):
    if roll[i]==data:
        temp=i
print(name[temp])
del(dict[1])


