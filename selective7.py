salary=int(input("enter the salary"))
year=int(input("enter the year service"))
if(year>10):
    print("the bonus is",salary-salary*(10/100))
if(year>6)and(year<10):
    print("the bonus is",salary-salary*(8/100))
else:
    print("the bonus is",salary-salary*(5/100))
