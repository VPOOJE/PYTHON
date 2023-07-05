'''Consider the following list which contains the month with year  
years = ["January 2023", “February 2024”, March 2023”, "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
If you have noticed, for some months, the year was wrongly mentioned instead of 2023. Write a Python program to change the month to 2023.'''
l = ["January 2023", "February 2024", "March 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
for i in range(len(l)):
    if "2024" in l[i]:
        l[i]=l[i].replace("2024","2023")
    elif "2025" in l[i]:
        l[i]=l[i].replace("2025","2023")
print(l)
        
        
        
        
