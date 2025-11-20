n = int(input("Въведете число: "))

print("Делители:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
