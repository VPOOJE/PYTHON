'''Ratings will be: 1 is bad, 2 is not bad, 3 is average, 4 is good, and 5 is excellent.
Read Food Rating: 1-5 
Read Service Rating: 1-5
Read Ambience Rating: 1–5
Read the bill's amount.
If the food is good or excellent:
Service and ambience are also good or excellent.
Then the tip is 10% of your bill amount.
Service and ambience are average/okay/bad.
Then the tip is 5% of your amount.
If the food is average, okay, or bad:
Service and ambience are also good or excellent.
Then the tip is 5% of your bill amount.
Service and ambience are average/okay/bad.
Then the tip is 1% of your bill amount.'''
bill=int(input("enter the bill amount"))
food=int(input("enter the food rating"))
service=int(input("enter the service rating"))
ambience =int(input("enter the ambience rating"))
if((food==4)or(food==5)):
    if((service==(4 or 5))and(ambience==(4 or 5))):
        print("the tip is",bill*(10/100))
    else:
        print("the tip is",bill*(5/100))
if((food==1)or(food==2)or(food==3)):
    if((service==(4 or 5))and(ambience==(4 or 5))):
        print("the tip is",bill*(5/100))
    else:
        print("the tip is",bill*(1/100))
    



