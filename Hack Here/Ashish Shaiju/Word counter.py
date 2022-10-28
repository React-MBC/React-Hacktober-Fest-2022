# ---Words Counter---

str = input("Enter the Sentence: ")

# Count words
words = len(str.split())

# Character counter
count = len(str)

print(f"""No of Words = {words} \n No of Characters = {count}""")