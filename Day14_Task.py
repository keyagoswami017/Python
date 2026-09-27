# Higher Lower Game

from Day14_GameData import data
import random

# Formatting the data printing
def format_data(info):
    name = info["name"]
    desc = info["description"]
    return f"{name}, a {desc}"

# Guess the follower count
def check_ans(selection, a_followers_count, b_followers_count):
    if selection == "a" and a_followers_count > b_followers_count:
        return True
    elif selection == "b" and a_followers_count < b_followers_count:
        return True
    else:
        return False


def high_lower():
    flow = True
    point = 0
    b = random.choice(data)
    while flow:
        a = b
        b = random.choice(data)

        # Re choice so that the values are not same
        if a == b:
            b = random.choice(data)

        print(f"Compare A : {format_data(a)}")
        print("VS")
        print(f"Against B : {format_data(b)}")

        choice = input("who has more followers 'A' or 'B': ").lower()

        a_followers = a["follower_count"]
        b_followers = b["follower_count"]

        check = check_ans(choice, a_followers, b_followers)
        if check:
            point = point + 1
            print(f"You are right, Score : {point}")
        else:
            print(f"You Lose, Score : {point}")
            flow = False


high_lower()