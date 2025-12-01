user_input = input("Enter words separated by space: ")
a = user_input.split()

res = [a[i:j] for i in range(len(a)) for j in range(i + 1, len(a) + 1)]  

print(res)