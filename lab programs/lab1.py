n=int(input("enter the no:"))
if n%2==0:
    rev=0
    temp=n
    while(n>0):
       digit=n%10
       rev=rev*10+digit
       n=n//10
    if(temp==n):
        print("palindrome")
    else:
        print("not a pallindrome")
else:
    def factorial(n):
      if n==1:
         return n
      else:
         return n*factorial(n-1)
    print("factroial is",  factorial(n))
    count=0
    n=factorial(n)
    while(n>0):
      n=n//10
      count=count+1
    print(count)

