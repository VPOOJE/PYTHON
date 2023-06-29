input = [2, 4, 8, 7, 5]
output = []

for num in input:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    output.append(factorial)
print(output)
