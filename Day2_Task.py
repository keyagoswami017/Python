print("Welcome to the Tip Calculator")
bill = float(input("What's the total bill? $\n"))
tip = float(input("How much tip would you like to give >? 10, 12 or 15\n"))
people = float(input("How many people to split the bill ?\n"))

total = bill + ((tip  * bill) / 100)
pay = total / people
print("Each person sho1uld pay $",round(pay,2))