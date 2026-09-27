from os import system

def auction_prog():
    print("Welcome to the secret auction program")
    name_bid_dict = {}
    proceed = True
    while proceed:
        name = input("What is your name?\n")
        bid = int(input("What is your bid?\n"))
        name_bid_dict[name] = bid
        choice = input("Are there any other biders? (yes/no)\n")
        if choice == "no":
            proceed = False
        else:
           print("\n" * 100)

    high_bid = 0
    name = ""
    for item in name_bid_dict:
        if name_bid_dict[item] > high_bid:
            name = item
            high_bid = name_bid_dict[item]

    print(f"Highest Bidding goes to {name} for bid {high_bid}")


auction_prog()