'''Given the dictionary that contains Key as “Cricketer Name”, and Value as dictionary of {Total Runs Conceded and Wickets} taken by 6 different players, 

Cricketer = {”VinayKumar”:{102,5},Yuzvendra Chahal : {89,10}, Sandeep Sharma : {95,8}, Umesh Yadav : {85,6}, “BhuvaneswarKumar”:{106,10}, Basil Thampi : {70,5}}

calculate the average bowling score using below Formula
Bowling Average = Total Runs Conceded / Total Wickets Taken
Replace the key values with the calculated Bowling Average.
Then sort the dictionary based on the Bowling Average.
Output
must be sorted based on the the value
{”VinayKumar”:{20.4},Umesh Yadav : {14.6}, Basil Thampi : {14}, Sandeep Sharma : {11.85}, “BhuvaneswarKumar”:{10.6}, Yuzvendra Chahal : {8.9}}

Sorted() function syntax to sort the value based on the key
sorted_dict = sorted(dictionary.items(), key=lambda x: x[1])
1st argument - dictionary.items() returns key,value pairs of the given dictionary
2nd argument - key parameter -> set to lambda x:x[1] refer to the value in pair therefore the dictionary will be sorted based on the value.'''
Cricketer = {
    "VinayKumar": {102, 5},
    "Yuzvendra Chahal": {89, 10},
    "Sandeep Sharma": {95, 8},
    "Umesh Yadav": {85, 6},
    "BhuvaneswarKumar": {106, 10},
    "Basil Thampi": {70, 5}
}
for cricketer, stats in Cricketer.items():
    runs_conceded, wickets_taken = stats
    bowling_average = runs_conceded / wickets_taken
    Cricketer[cricketer] = round(bowling_average, 2)
sorted_dict = sorted(Cricketer.items(), key=lambda x: x[1])
sorted_cricketer_dict = {k: v for k, v in sorted_dict}
print(sorted_cricketer_dict)






