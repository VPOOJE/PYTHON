
'''Write a python program that has a list of positive and negative numbers.Make a new tuple that has only positive values from the list.
Sample Input: (-20,-4,-7,6,4,8,3,-6)
Sample Output: (6,4,8,3)'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
prime_numbers = set(num for num in range(1, 51) if is_prime(num))
divisible_by_5 = set(num for num in range(1, 51) if num % 5 == 0)
union_set = prime_numbers.union(divisible_by_5)
intersection_set = prime_numbers.intersection(divisible_by_5)
difference_set = prime_numbers.difference(divisible_by_5)
symmetric_difference_set = prime_numbers.symmetric_difference(divisible_by_5)
print("Union Set:", union_set)
print("Intersection Set:", intersection_set)
print("Difference Set:", difference_set)
print("Symmetric Difference Set:", symmetric_difference_set)
