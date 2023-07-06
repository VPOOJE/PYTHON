

'''Write a Python Program to Count the Number of Vowels
in a Given String Using Sets. Don’t use any built in string functions. 
Hint: Create a set that contains VOWELS'''


def count_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count
input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print("Number of vowels:", vowel_count)
