import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
choice1 = int(input("Enter your selection:"))

choice2 = random.randint(0,2)
print("Comp Choice :", choice2)
if (choice1 == 0 and choice2 == 0) or (choice1 == 1 and choice2 == 1) or (choice1 == 2 and choice2 == 2) :
    print("You chose Rock")
    print("Comp chose Rock")
    print("Match Draw")
elif (choice1 == 0 and choice2 == 1) or (choice1 == 1 and choice2 == 2) or (choice1 == 2 and choice2 == 0):
    print("You chose Rock")
    print("Comp chose Paper")
    print("Comp Win")
elif (choice1 == 0 and choice2 == 2) or (choice1 == 1 and choice2 == 0) or (choice1 == 2 and choice2 == 1):
    print("You chose Rock")
    print("Comp chose Scissors")
    print("You Win")
else:
    print("Wrong Choice")