# Blackjack Project
import random

# select a card from deck
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

# calculate cards sum
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# compare the user and computer score
def compare_score(u_score, c_score):
    if u_score == c_score:
        return "Draw!!!"
    elif c_score == 0:
        return "Lose, Opponent has Blackjack!!!"
    elif u_score == 0:
        return "Win, You have a Blackjack!!!"
    elif u_score > 21:
        return "You went over. You Lose!!!"
    elif c_score > 21:
        return "Opponent went over. You Win!!!"
    elif u_score > c_score:
        return "You win!!!"
    else:
        return "You Lose!!!"


def play_game():
    user_card = []
    comp_card = []
    is_game_over = False
    comp_score = -1
    user_score = -1

    for _ in range(2):
        user_card.append(deal_card())
        comp_card.append(deal_card())
    while not is_game_over:
         user_score = calculate_score(user_card)
         comp_score = calculate_score(comp_card)
         print(f" User's hands: [{user_card}], User's score: {user_score} ")
         print(f" Computer's first hand: [{comp_card[0]}] ")

         if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True

         else:
             user_should_deal = input("Type 'y' to get another card, type 'n' to pass:\n")
             if user_should_deal == "y":
                 user_card.append(deal_card())
             else:
                 is_game_over = True

    while comp_score != 0 and comp_score < 17:
         comp_card.append(deal_card())
         comp_score = calculate_score(comp_card)

    print(f" User's final hand: [{user_card}] ")
    print(f" Computer's final hand: [{comp_card}] ")

    print(compare_score(user_score,comp_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n") == "y":
    print("Welcome to Blackjack!")
    print("\n" * 30)
    play_game()

