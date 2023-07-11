




'''Write a Python program to check if a set is a subset of another set.
WITHOUT USING issubset function()
Sample Input 
a={1,2,3,4}
b={1,2,3}
Sample Output 
True'''


a={1,2,3,4}
b={1,2,3}
print("Checking whether a is subset of b...... \n")
if(a.issubset(b)==True):
 print("The set a is the subset of set a \n")
else:
 print("The set a is not the subset of set b \n")
print("Checking whether b is subset of a...... \n")
if(b.issubset(a)==True):
 print("The set b is the subset of set a \n")
else:
 print("The set b is not the subset of set a \n")
