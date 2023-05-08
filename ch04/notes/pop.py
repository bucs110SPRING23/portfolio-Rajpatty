# Iteration

# mystr = "hello"


# for ch in mystr:
    # print(ch)

# for num in mynums:
    # print(num)

# print(mystr[0],mystr[1],mystr[2],mystr[3],mystr[4])

# mynums[0] = 5
# print(mynums)

# print(mystr[0])
# print(mystr[1:4])

# mystr = "J" + mystr[1:5]
# print(mystr)

mynums = [1, 2, 3, 4, 5]

mynums[2:2] = [2.5,2.6]
print(mynums)

for i, v in enumerate(mynums):
    mynums[i] = v * 2

print(mynums)

i = 0
while i < 10:
    print(i)
    i += 3

print("Enter numbers to sum [q to quit]:")
sum = 0
while True:
    value = input("number:")
    if value.isdigit():
        value = int(value)



