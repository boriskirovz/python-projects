start = int(input("Начало: "))
end = int(input("Край: "))

for i in range(start + 1, end):
    if i % 2 == 1:
        print(f"Първото нечетно число в интервала {start}, {end} е: {i}")
        break
