numbers = list(map(int, input("Въведете числа, разделени с интервал: ").split()))

for num in numbers:
    if num < 0: numbers.remove(num)

print(numbers)