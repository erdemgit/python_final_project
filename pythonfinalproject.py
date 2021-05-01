from random import choice

def main():
    bet = 0
    dest = {
        "A": [11, 4], "2": [2, 4], "3": [3, 4], "4": [4, 4], "5": [5, 4], "6": [6, 4], "7": [7, 4], "8": [8, 4], "9": [9, 4], 
        "1": [10, 4], "J": [10, 4], "Q": [10, 4], "K": [10, 4]
        }
    cards = "A234567891JQK"
    bet = takethebet()
    player_hand = firsthand(cards, dest)
    if isitblackjack(player_hand): playerwins(bet) 
    case_hand = firsthand(cards, dest)
    if isitblackjack(case_hand): casewins(bet)
    print("{}".format(case_hand[0]))
    exit()

def casewins(bet):
    print("Sorry, you just lost: {}".format(bet))
    exit()

def playerwins(bet):
    print("You won {}".format(bet*2))
    exit()

def isitblackjack(hand):
    if "A" == hand[0]:
        if hand[1] in "1JQK":
            print("Blackjack: {}".format(hand))
            return True
    elif "A" == hand[1]:
        if hand[0] in "1JQK":
            print("Blackjack: {}".format(hand))
            return True
    return False

def firsthand(cards, dest):
    hand = ""
    for _ in range(2):
        card = choice(cards)
        if dest[card][1] > 0:
            hand += card
            dest[card][1] -= 1
    return hand

def takethebet():
    return int(input("Welcome, bet please: "))

main()

