
from datetime import datetime

'''...A date in Python is not a data type of it's own, But we can import a module named date-time to work with date as date object '''

# x = datetime.now()
# print(x)
# print(x.year)



# x = datetime(2020,5,17)
# print(x)

# strftime(): String format time method , This method takes one parameter format of the specified format of the returned string 

x = datetime.now()
print(x)
print(x.strftime("%a"))  # weekday short version
print(x.strftime("%A"))  # weekday full version
print(x.strftime("%w"))  # weekday 0-6 , 0-sunday,1-monday.....6-saturday
print(x.strftime("%d"))  # day of month
print(x.strftime("%b"))  # month name-short version
print(x.strftime("%B"))  # month name-full version
print(x.strftime("%m"))  # month as a number 1-12
print(x.strftime("%y"))  # Year short version
print(x.strftime("%Y"))  # Year full version
print(x.strftime("%H"))  # Hour 0-23
print(x.strftime("%I"))  # Hour 0-12
print(x.strftime("%p"))  # AM/PM
print(x.strftime("%M"))  # Minutes
print(x.strftime("%S"))  # Seconds