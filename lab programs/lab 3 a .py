n=int(input("enter the no"))
l=list()
for i in range(0,n):
    k=int(input("no"))
    l.append(k)
print(l)
flag=0
l1 = l[:]
l1.sort()
if (l1 == l):
 flag = 1
if(not flag):
    print("accending order")
else:
    print("decending order")


