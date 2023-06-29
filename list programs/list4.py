'''Write a python program that reads the string, encode each character in a string using ascii values and store the ascii value in the list. The program reads the strings from the user, and stores the individual characters ascii value to the list
Sample Input
Enter the string : Science
Sample Output
Encode the List - [83, 99, 105, 101, 110, 99, 101]
Note: Use ord() function'''
string=input("enter the string:")
n=[]
for i in string:
    n.append(ord(i))
print(n)
