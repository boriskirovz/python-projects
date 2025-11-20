n = str(input("enter: "))
even=[]
odd=[]

for char in n:
    char = int(char)
    if  char % 2 == 0:
        even.append(char)
    else: odd.append(char)

print(even)
print(odd)