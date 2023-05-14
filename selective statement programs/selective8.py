name=input("enter the name:")
age=int(input("enter the age"))
gender=input("enter the gender")
g=gender.upper()
days=int(input("no of days"))
if(age>=18)and(age<30)and(gender=="M"):
    print("the wages will be",days*700)
if(age>=18)and(age<30)and(gender=="F"):
    print("the wages will be",days*750)
if(age>=30)and(age<=40)and(gender=="M"):
    print("the wages will be",days*800)
if(age>=30)and(age<=40)and(gender=="F"):
    print("the wages will be",days*800)
    
