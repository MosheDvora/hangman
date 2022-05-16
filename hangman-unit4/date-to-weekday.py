import calendar

date_input = input("Enter a date\n")
date_input = date_input.split("/")
day = calendar.weekday(int(date_input[2]), int(date_input[1]), int(date_input[0]))
print(calendar.weekday(2000, 1, 1))
wday = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Weekday name", wday[day])