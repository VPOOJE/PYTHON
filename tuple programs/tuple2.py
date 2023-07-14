'''Write a python program that has a list of positive and negative numbers.Make a new tuple that has only positive values from the list.
Sample Input: (-20,-4,-7,6,4,8,3,-6)
Sample Output: (6,4,8,3)'''
n=(-20,-4,-7,6,4,8,3,-6)
s=tuple(i for i in n if i>0)
print(s)
