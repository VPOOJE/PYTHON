'''Write a program to accept the numbers continuously;
when we enter"-1” it should stop accepting the input
and at the same time display the number of even numbers
and odd numbers that were entered.'''
count_even=0
count_odd=0
num=0
while(num!=(-1)):
    num=int(input("enter the number="))
    if(num%2==0):
        count_even+=1
    else:
        count_odd+=1
        
print(count_even)
print(count_odd-1)
    
        


