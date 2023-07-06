'''Generate a dictionary where keys are numbers and values consist
of a set of its factors in a specified range. 
Factors = {1:{1} , 2:{1,2}, 3: {1,3}, 4:{1,2,4} , 5:{1,5}, 6:{1,2,3,6},
7:{1,7}, 8:{1,2,4,8}, 9:{1,3,9,}}'''
start= 1
end= 9
factor = {num: {i for i in range(1, num+1) if num % i == 0} for num in range(start, end+1)}

for number, factors in factor.items():
    print(number, ":", factors)

