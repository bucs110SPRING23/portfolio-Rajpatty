c = int(input("How many rows?"))

print(c)

for i in range(c):
    for j in range(i+1):
        print("*",end = "")
    print("\n")

