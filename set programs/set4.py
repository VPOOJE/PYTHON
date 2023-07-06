'''Consider the given list and find the common elements
of the three given lists USING SET.
List1 = [10, 45, 34, 20, 11]
List2 = [11, 25, 45, 20]
List3 = [20, 25, 11, 14, 45, 65]'''
def find_common_elements(list1, list2, list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    common_elements = set1.intersection(set2, set3)
    return common_elements
list1 = [10, 45, 34, 20, 11]
list2 = [11, 25, 45, 20]
list3 = [20, 25, 11, 14, 45, 65]
common_elements = find_common_elements(list1, list2, list3)
print("Common Elements:", common_elements)

