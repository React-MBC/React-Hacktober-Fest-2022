import random

letters = ['a','b','c','d','e','F','G','H']
symbols = ['!','@','#']
numbers = ['1','2','3','4']

print("welcome to password generator")
nr_letters = int(input("no of letters in password!!\n"))
nr_symbols = int(input("no of symbols!\n"))
nr_numbers = int(input("no of numbers!\n"))

password_list = []
for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols+1):
    password_list += random.choice(symbols)
for char in range(1, nr_numbers+1):
    password_list += random.choice(numbers)

password = ""
for char in password_list:
    password += char

print(f"your passsword is:{password}")