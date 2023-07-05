'''A program should read “n” positive integers from the user and
append it to the list, and if the list contains prime numbers return “True” and
number of prime numbers, else “False”.'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter the number of integers: "))

num_list = [int(input("Enter number ")) for i in range(n)]

prime_numbers = [num for num in num_list if is_prime(num)]

if prime_numbers:
    print("True")
    print("Number of prime numbers:", len(prime_numbers))
else:
    print("False")
