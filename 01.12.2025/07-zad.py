def find_max_number(num_list):
    if not num_list:
        return None
    return max(num_list)

user_input = input("Enter numbers separated by space: ")
numbers = [int(x) for x in user_input.split()]

print(f"Max number: {find_max_number(numbers)}")