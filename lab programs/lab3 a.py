

n=int(input("Enter number of elements in list: "))
l=list()
for i in range(0,n):
 e=input("Enter the value: ")
 l.append(e)
 
print(l)
k=input("Enter the element to be searched in the list: ")
res=len(l)-l.index(k)
print("The required Positive index : ",l.index(k))
print("The required Negative index : -",str(res))
