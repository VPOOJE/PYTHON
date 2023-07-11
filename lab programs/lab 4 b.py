
'''Write a python program to reverse a tuple
Sample Input 
tuples = ('a','b','c','d','e','f','g','h')
Sample Output 
('h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')'''



def str(t):
 res=t[::-1]
 return res
n=int(input("enter the no"))
l=list()
for i in range(0,n):
    e=str(input("input"))
    l.append(e)
a=tuple(l)
print(str(a))
    
    
