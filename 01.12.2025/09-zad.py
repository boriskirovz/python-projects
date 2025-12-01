def count_even_numbers(num_list):
    count = 0
    for num in num_list:
        if num % 2 == 0:
            count += 1
    return count

user_input = input("Enter numbers separated by space: ")
numbers = [int(x) for x in user_input.split()]

print(f"Count of even numbers: {count_even_numbers(numbers)}")