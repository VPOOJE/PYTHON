'''Write a program to display the prime in the given range. 
Sample Input
1
10
Sample Output
2 , 3 , 5 , 7'''

for i in range(1,11):
    count=1
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                 count=0
                 break
        if(count==1):
            print(i)
            
            
