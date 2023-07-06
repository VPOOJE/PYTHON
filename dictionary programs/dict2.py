'''Write a program that inverts a dictionary. I.e., it makes key of one dictionary value of another and vice versa
Sample Input:
Dict={‘Reg.No”:123, ‘Name’:’abc’,Course’:’CSE’}
Sample Output:
Inv Dict={123:’Reg.No’, ‘abc’ : ‘Name’, ‘CSE’: ‘Course’}'''
def invert_dict(dictionary):
    inv_dict = {value: key for key, value in dictionary.items()}
    return inv_dict
dict = {'Reg.No': 123, 'Name': 'abc', 'Course': 'CSE'}
inv_dict = invert_dict(dict)
print("Inv Dict =", inv_dict)

