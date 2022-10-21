def leap_year_checker(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year")
            else:
                print('not Lear Year')
        else:
            print('leaP year')
    else:
        print('not leap year')


leap_year_checker(2004)