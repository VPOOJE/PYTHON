'''Write a python program which reads “n” words from the user,
store it in the list and display the length of each word and display
the longest word in the list.'''
n=[]
s=int(input("enter the no of words"))
for i in range(s):
    string=input("enter the words")
    n.append(string)
print(n)
for s in n:
    print(f"{s}: {len(s)}")
largest = max(n)
print("longest word:",largest)

    
