'''Write a program to display the count of even and odd numbers in a given range.
Sample Input
Start: 20
End : 50
(inclusive of 20 and 50)
Sample Output:
Even : 16
Odd : 15'''
odd_count=0
even_count=0
for i in range(20,51):
    if(i%2==0):
        even_count+=1
    else:
        odd_count+=1
print(even_count)
print(odd_count)




















