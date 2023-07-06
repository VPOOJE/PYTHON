'''Write a python program that has a list of positive and negative numbers.Make a new tuple that has only positive values from the list.
Sample Input: (-20,-4,-7,6,4,8,3,-6)
Sample Output: (6,4,8,3)'''
def get_positive_numbers(numbers):
    positive_numbers = tuple(num for num in numbers if num > 0)
    return positive_numbers
number_list = (-20, -4, -7, 6, 4, 8, 3, -6)
positive_tuple = get_positive_numbers(number_list)
print(positive_tuple)
