
'''Write a python program to generate the following dictionary 
Num = { 1 : 1, 2 : 8, 3 : 27, 4 : 64, 5 : 125 ….. , 20 : 8000}'''

num = {}
for i in range(1, 21):
    num[i] = i ** 3

print(num)
