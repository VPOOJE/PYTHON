

'''Write a program to display the prime in the given range. 
Sample Input
1
10
Sample Output
2 , 3 , 5 , 7'''
l=[]
for i in range(1,10):
    for j in range(2,i):
        if i % j==0:
           break
    else:
      l.append(i)
print(l)
