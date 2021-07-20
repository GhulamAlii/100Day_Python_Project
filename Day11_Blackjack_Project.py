##################  Blackjack Game  ###########
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    select_card = random.choice(cards)
    return select_card



def calc_point(cards):
    if sum(cards) == 21 and len(cards) ==2:
        return 0

    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def Compare(user_score,comp_score):

    if user_score == comp_score:
        return "You both have same Score the match is Draw"
    elif comp_score == 0 :
        return "you lose Opponent Has a Blackjack"

    elif user_score == 0 :
        return "Congratulation You  win with a blackjack 🎉 🎉"

    elif user_score >21:
        return "you lose Your score go over"
    elif comp_score >21:
        return "Opponent score go over. Congratulation You  win 🎉 🎉"
    elif user_score > comp_score:
        return "Congratulation You  win 🎉 🎉"
    else:
        return "you Lose"

def main_game():
    user_card = []
    comp_card = []
    gameOver = False


    for _ in range(2):
        user_card.append(deal_card())
        comp_card.append(deal_card())

    while not gameOver:
        user_score = calc_point(user_card)
        com_score = calc_point(comp_card)

        print(f" your card:{user_card}, current score:{user_score}")
        print(f" Computer First card:{comp_card[0]}")


        if user_score == 0 or com_score == 0 or user_score >21:

           gameOver = True

        else:
            usr_inp = input("you want to draw another card? Y/N").lower()
            if usr_inp == "y":
                user_card.append(deal_card())
            else:
                gameOver = True


    while com_score != 0 and com_score<17:
          comp_card.append(deal_card())
          com_score = calc_point(comp_card)

    print(f"Your Score is {user_score} and the pc score is {com_score}")
    print(Compare(user_score, com_score))

while input("Do you Want to play  So Press Y/N").lower() == "y":
    main_game()