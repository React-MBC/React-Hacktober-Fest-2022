mport random
rock="""
    ___
---'   __)
      (___)
      (___)
      (__)
---._(__)
"""

paper="""
     ___
---'    _)_
           __)
          ___)
         ___)
---.____)
"""

scissor="""
    ___
---'   _)_
          __)
       ____)
      (__)
---._(__)
"""

game_images = [rock, paper, scissor]
user_choice = int(input("Enter 0 for rock, 1 for paper and 2 for scissor:"))
print(f"USER CHOICE:{game_images[user_choice]}")
computer_choice = random.randint(0, 2)
print(f"COMPUTER CHOICE:{game_images[computer_choice]}")

if user_choice == computer_choice:
    print("it's a draw!")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif user_choice == 1 and computer_choice == 0:
    print("you win!")
elif user_choice == 2 and computer_choice == 1:
    print("you win!")
else:
    print("you lose!")