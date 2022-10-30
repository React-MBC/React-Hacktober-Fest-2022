# Leap Year Checker

year = int(input("\n\tLeap year checker\n\n Enter year: "))
if year % 400 == 0:
    print("\n Leap Year\n")
elif year % 4 == 0:
    print("\n Leap Year\n")
elif year % 100 == 0:
    print("\nNot Leap Year\n")
else:
    print("\nNot Leap Year\n")
