'''Write a program to display the factors of a given number.
Sample Input
56
Sample output
1, 2, 4, 7, 8, 14, 28, 56'''
num=int(input("enter the number:"))
for i in range(1,num+1):
    if(num%i==0):
        print(i)
    else:
        pass


