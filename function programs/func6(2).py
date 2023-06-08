'''x/2 + x/4 + x/8 + x/16 + ….. + N
  Sample Input
N = 7 (Number of terms)
X = 2
Then the series will be 2/2 + 2/4 + 2/8 + 2/16 + 2/32 + 2/64 + 2/128
Sample Output:'''

def calculate_series_sum():
    sum = 0
    denominator = 2

    for i in range(7):
        sum += 2 / denominator
        denominator *= 2

    return sum

result = calculate_series_sum()
print(result)
