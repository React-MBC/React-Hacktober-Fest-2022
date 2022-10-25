Sum = 0

print("Please Enter 10 Numbers\n")
for i in range(1, 11):
    num = int(input("Number %d = " %i))
    Sum = Sum + num

avg = Sum / 10

print("The Sum of 10 Numbers     = ", Sum)
print("The Average of 10 Numbers = ", avg)