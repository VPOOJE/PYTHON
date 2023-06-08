'''15 + 30 + 45 + 60 + …… + N
Sample Input
N = 5 (Number of terms)
Sample Outpu'''
def calculate_series_sum():
    sum = 0
    common_difference = 15
    num_terms = 5

    for i in range(num_terms):
        term = common_difference * (i + 1)
        sum += term

    return sum

result = calculate_series_sum()
print(result)
