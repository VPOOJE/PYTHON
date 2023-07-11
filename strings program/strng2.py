def swap_strings(string1, string2):
    swapped_string1 = string2[:2] + string1[2:]
    swapped_string2 = string1[:2] + string2[2:]
    return swapped_string1 + ' ' + swapped_string2

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = swap_strings(string1, string2)
print("Swapped string:", result)
