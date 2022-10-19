print("welcome to bill calculator")
bill = float(input("total bill? $"))
tip = int(input("tip percentage? 10,12or15:"))
people = int(input("how many to split the bill?"))
bill_with_tip = tip/100*bill+bill
bill_with_person = bill_with_tip/people
final_amount = round(bill_with_person,2)
print(f"each should pay:${final_amount}")