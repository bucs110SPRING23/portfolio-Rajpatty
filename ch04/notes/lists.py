## tuple - immutable list
mynums = (5,8,1) # immutable
print(list(enumerate(mynums)))

x = 5 
y = 6
x,y = y,x

num = [5] * 3
print(num)

x,y = (5,6)
for i, v in enumerate(mynums):
    print(i,v)

contacts = {"bill": "867-9823", "jane": "555-1212",}
    
## name = input("enter a name:")

## for contact in contacts:
    # if contact[0] == name:
        # print(contact[1])
       # break


## print(contacts[name])

contacts["joe"] = "555-1212"
print(contacts)

for key, value in contacts.items():
    print(key)
    print(value)

for key in contacts.keys():
    print(key)

for val in contacts.values():
    print(val)

if contacts.get("juan"):
    print(contacts["juan"])