'''Write a program that generates a set of squares of numbers in the range(1-30) and another list generates numbers
that are divisible by 3 in the range(1-30). Generate a newset from a square set,
which should not contain the numbers that are divisible by 3.'''
square = {num ** 2 for num in range(1, 31)}
list = [num for num in range(1, 31) if num % 3 == 0]
new_set = square - set(list)
print("New Set:", new_set)
