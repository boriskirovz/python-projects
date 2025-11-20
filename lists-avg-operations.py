numbers = list(map(int, input("Enter numbers: ").split()))
avg = 0
listBiggerThanAVG = []

for num in numbers:
    avg += num

avg = avg/len(numbers)
print("Avg is", avg)

for num in numbers:
    if num > avg:
        listBiggerThanAVG.append(num)


print(listBiggerThanAVG)