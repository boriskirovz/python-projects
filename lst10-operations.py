lst_10 = [4, 12, 16, 42, 5, 8, 11, 7, 2, 1]

print("Enter 10 positive integers:")

while len(lst_10) < 10:
    try:
        num = int(input("Enter number: "))
        if num > 0:
            lst_10.append(num)
        else:
            print("The number must be positive. Try again.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("\nlst_10:", lst_10)

odd_number = 0
average = 0.0

for num in lst_10:
    average += num
    if num % 2 == 1:
        odd_number += 1

print(f"There are {odd_number} odd numbers")
print(f"The average is {average/len(lst_10)}")

lst_5 = []
lst_10 = sorted(lst_10, reverse=True) #tuk imam li pravo purvo da si sortiram tozi spisuk i taka da ne trqbwa da sortiram 2riq
i = 0

while len(lst_5) < 5:
    if lst_10[i] % 2 == 0:
        lst_5.append(lst_10[i])
    i += 1

print("lst_5:",  lst_5)

j = 0
while j < len(lst_5):
    if j % 2 == 0: #towa li se ima predvid pod da se premahne
        lst_5[j] = 0
    j += 1

print("lst_5:",  lst_5)