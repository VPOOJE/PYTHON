'''Write a python program to convert tuple to a string
Sample Input 
tuple=(‘p’, ‘ y’, ’t’,, ‘h’, ’o’, ’n’)
Sample Output
Python'''
def str(t):
   res=''
   for item in t:
       res=res+item
   return res
n=int(input("enter the no"))
l=list()
for i in range(0,n):
    e=str(input("input"))
    l.append(e)
a=tuple(l)
print(str(a))
