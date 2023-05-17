'''Write a program to display the Amstrong numbers in the given range
Enter lower range: 100
Enter upper range: 1000
The armstrong numbers are: 
153
370
371
407'''
lower = 100
upper = 1001

for num in range(lower, upper + 1):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)

        
