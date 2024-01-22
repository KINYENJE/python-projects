from datetime import date, datetime, timedelta

today = date.today()
print(type(today)) # <class 'datetime.date'>
print("Today's date is : " + str(today)) # Today's date is : 2024-01-22

current_time = datetime.now()
print(current_time) # 2024-01-22 21:04:04.102349

# strftime() method is used to create a string representing the date and time under the control of an explicit format string.
print(current_time.strftime('%d/%m/%Y %H:%M:%S')) # 22/01/2024 21:04:04

print(current_time.strftime('%A %d %B %Y')) # Monday 22 January 2024