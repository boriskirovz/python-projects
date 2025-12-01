def sum_greater_than_ten(num_list):
    total_sum = 0
    for num in num_list:
        if num > 10:
            total_sum += num
    return total_sum

user_input = input("Enter numbers separated by space: ")
numbers = [int(x) for x in user_input.split()]

print(f"Sum of numbers > 10: {sum_greater_than_ten(numbers)}")