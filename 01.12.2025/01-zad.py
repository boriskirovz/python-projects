user_input = input("Enter numbers separated by space: ")
numbers = [int(x) for x in user_input.split()]

max_number = max(numbers)

print(f"The largest number is: {max_number}")