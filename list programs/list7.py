'''Write a python program that removes duplicates from the given list
and generate
the new list without duplicates.'''
n=[2,5,2,6,3,4,5]
m=[]
for i in n:
    if i not in m:
        m.append(i)
print(m)
