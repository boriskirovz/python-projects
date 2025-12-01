user_input = input("Enter numbers separated by space: ")
numbers = [int(x) for x in user_input.split()]

limit = float(input("Enter the lower limit value: "))

average_value = sum(numbers) / len(numbers)

result = [x for x in numbers if x < average_value and x > limit]

print(f"Average value: {average_value}")
print(f"Elements < average and > {limit}: {result}")