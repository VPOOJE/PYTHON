

def is_perfect_square(num):
    square=int(num**0.5)
    return square*square==num
n=int(input("enter the no"))
if is_perfect_square(n):
    print("perfect square")
else:
    print(" not perfect square")
    
