'''Write a python program that reads integers from the user
and stores them in a list. Your program should continue reading
values until the user enters 0. Then it should display all of the
values entered by the user (except for the 0) in ascending order
(The list itself to be sorted).'''

n = []
while True:
    num = int(input("Enter an integer (enter 0 to stop): "))
    if num == 0:
        break
    n.append(num)
print(n)
n.sort()
print("Sorted list of values:")
for num in n:
    print(num)
