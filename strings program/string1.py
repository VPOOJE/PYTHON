'''Write a Python program to get a string made of the first 2 and last
2 characters of a given string.
If the string length is less than 2, return the empty string instead.'''
def get_string(string):
    if len(string) < 2:
        return ''
    else:
        return string[:2] + string[-2:]


input_string = input("Enter a string: ")
result = get_string(input_string)
print("Result:", result)
        
