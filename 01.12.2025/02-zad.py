user_input = input("Enter words separated by space: ")
words = user_input.split()

long_words = [word for word in words if len(word) > 5]

print(f"Words longer than 5 letters: {long_words}")