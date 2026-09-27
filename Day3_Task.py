print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
Choice1 = input('Type "left" or "right"').lower()
if Choice1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2 = input('Type "wait" to wait for the boat. Type "swim" to swim across').lower()
    if choice2 == "wait":
        print("You arrived at the island. There is a house with 3 doors")
        choice3 = input( "One Red, One Yellow, One Blue. which one would you chooseL").lower()
        if choice3 == "red":
            print("Game over")
        elif choice3 == "yellow":
            print("Game over")
        elif choice3 == "blue":
            print("You Win!!!")
        else:
            print("Wrong Choice!! Game Over")
    else:
        print("Game over")
else:
    print("Game over")