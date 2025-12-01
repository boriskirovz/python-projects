word_one = input("Enter the first word: ")
word_two = input("Enter the second word: ")

if sorted(word_one.lower()) == sorted(word_two.lower()):
    print("The words are anagrams.")
else:
    print("The words are NOT anagrams.")