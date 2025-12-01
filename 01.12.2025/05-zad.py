user_input = input("Enter numbers separated by space: ")
numbers = [int(x) for x in user_input.split()]

average_value = sum(numbers) / len(numbers)
above_average = [x for x in numbers if x > average_value]

print(f"Average value: {average_value}")
print(f"Numbers greater than average: {above_average}")