score = 0
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("okay! Let's play :)")


answer = input("What doea CPU stand for?\n")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What doea GPU stand for?\n")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What doea RAM stand for?\n")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What doea PSU stand for?\n")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What doea GUI stand for?\n")
if answer.lower() == "graphical user interface":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What doea ROM stand for?\n")
if answer.lower() == "read only memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/6)*100) + " %.")
