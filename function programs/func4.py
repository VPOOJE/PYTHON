'''Write a python code to find the nth term of the fibonacci series using RECURSION.
Sample Input:
5
Sample Output:
3'''
def fibonacci(n):
    if n<=0:
        print("invalid")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))    
