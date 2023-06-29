'''Write a python program which reads “n” number of integers
from the user and generates a separate list
containing even and odd numbers.'''
n = int(input("Enter the value of n: "))
even_numbers = []
odd_numbers = []
for i in range(n):
    num = int(input("Enter an integer: "))
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
