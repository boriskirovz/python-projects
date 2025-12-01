user_input = input("Enter numbers separated by space: ")
numbers = [int(x) for x in user_input.split()]

evens = []
odds = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print(f"Even numbers: {evens}")
print(f"Odd numbers: {odds}")