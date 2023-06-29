mail=input("enter your mail id:")
a=mail.split("@")[0]
print("the username is",a)
b=a[::-1]
c=str.upper(b)
print("the password is",a+c)


