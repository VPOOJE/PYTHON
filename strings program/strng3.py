sentence = input("Enter a sentence: ")

longest_word = max(sentence.split(), key=len)
length = len(longest_word)

print("Longest word:", longest_word)
print("Length of the longest word:", length)
