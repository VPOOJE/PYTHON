'''Write a python code with function interest_calculation() which calculates the simple interest.
The program should take the name of the customer, age of the customer, gender (‘M’ of ‘F’),
principal amount(P) and number of years (N) as an input.
If the customer is a senior citizen, fix the rate of interest (R) at 12%,
if the customer is “female,” fix the rate of interest (R) at 10%; and for others,
fix the rate of interest (R) at 9%.
The function should take P, N, and R values as parameters. '''
def simple_interst(p,n,r):
    z=p*n*r/100
    return z

name=input("enter the name")
age=int(input("enter the age"))
gender=input("enter the gender")
p=int(input("enter the principal amount"))
n=int(input("enter the no of years"))
r=float(input("enter the rate of interst"))
si=simple_interst(p,n,r)
print("the simple interst is",si)
