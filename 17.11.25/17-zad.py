year = input("Въведи година: ")

if year % 400 == 0:
    print("Високосна")
elif year % 100 == 0:
    print("Невисокосна")
elif year % 4 == 0:
    print("Високосна")
else: print("Невисокосна")