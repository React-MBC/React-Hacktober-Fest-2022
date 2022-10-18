import calendar

y = 2014  
m = 11

yy = int(input(f"Enter The Year (eg: {y}): "))
mm = int(input(f"Enter The Month (eg: {m}): "))

print(calendar.month(yy, mm))
