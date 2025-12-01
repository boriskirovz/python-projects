input1 = input("Enter the first list of elements: ")
input2 = input("Enter the second list of elements: ")

list_one = input1.split()
list_two = input2.split()

common_elements = list(set(list_one) & set(list_two))

print(f"Common elements: {common_elements}")