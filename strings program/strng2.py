'''Write a Python function that takes a sentence and returns
the longest word and the length of the longest one'''


def longest_word(sentence):
    words = sentence.split()
    longest = ''
    length = 0

    for word in words:
        if len(word) > length:
            longest = word
            length = len(word)

    return longest, length

input_sentence = input("Enter a sentence: ")
result_word, result_length = longest_word(input_sentence)
print("Longest word:", result_word)
print("Length of the longest word:", result_length)









      
