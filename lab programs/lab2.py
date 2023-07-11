s1=str(input("enter the str:"))
s2=str(input("enter the str:"))
s3=""
temp=0
l1=len(s1)
l2=len(s2)
for i in range(0,l2):
    for j in range(temp,l1):
        if(s2[i]==s1[j]):
            s3=s3+s1[j]
            temp=j+1
            break
if(s2==s3):
    print("yes")
else:
    print("no")
        
