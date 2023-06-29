'''Write a python program to remove even numbers from the given list.
Sample Input:
[5,6,2,8,9,12,66]
Sample Output
[5,9] '''
n=[5,6,2,8,9,12,66]
m=[]
for i in n:
    if(i%2==1):
        m.append(i)
print(m)
        
        
