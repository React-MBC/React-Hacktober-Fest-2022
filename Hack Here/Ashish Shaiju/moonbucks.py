# Moonbucks hotel program

name = input("\n\t\t\tWelcome to Moonbucks\n\nWhat is your Name: ")

# Menu
def menu(name):
    item = int(input("Menu is \n 1) Shrarjah Shake \n 2) Coffee \n 3) Smooothie \n 4) Ice Cream \n Choose your option from the above list \n"))
    num = int(input("How many items do you need: "))
    if item == 1:
        print(name + "Your Sharjah Shake will be available shortly....\n\n")
        print("Price of ", num, "Sharjah shake is $", num*8)
        exit()
    elif item == 2:
        print(name + "Your Coffee will be available shortly....\n\n")
        print("Price of ", num, "Coffee is $", num*8)
        exit()
    elif item == 3:
        print(name + "Your Smooothie will be available shortly....\n\n")
        print("Price of ", num, "Smooothie is $", num*8)
        exit()
    elif item == 4:
        print(name + "Your Ice Cream will be available shortly....\n\n")
        print("Price of ", num, "Ice Cream is $", num*8)
        exit()
    else:
        print("\nInvalid input\n")
        exit()

# Checks weather the user is named "Chris"or "Sharon"
if name.upper() == "CHRIS" or name.upper() == "SHARON":
    evil = input(name + ", Are you evil or not?(Y/N)\n")

    if evil.upper() == "YES" or evil.upper() == "Y":
        good_deeds = int(input("Enter the no of good deeds done today: "))
        if good_deeds<=3:
            print("\nSorry Evil " + name + ", You are not Welcomed here\n\n")
            exit()
        else:
            menu(name)
    else:
        menu(name)

else:
    menu(name)