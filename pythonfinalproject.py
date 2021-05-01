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
    print("Player Hand: {}".format(player_hand))
    
    case_hand = firsthand(cards, dest)
    if isitblackjack(case_hand): casewins(bet)
    print("Case Hand: {}".format(case_hand[0]))
    
    while doyouwanttodraw():
        player_hand += drawcard(cards, dest)
        print("Player cards: {}".format(player_hand))
        if isitover21(player_hand, dest): casewins(bet)
    
    print("Case cards: {}".format(case_hand))
    while shouldcasedrawcard(player_hand, case_hand, dest):
        case_hand += drawcard(cards, dest)
        print("Case cards: {}".format(case_hand))
        if isitover21(case_hand, dest): playerwins(bet)
    
    print("Player cards: {}\nCase cards: {}".format(player_hand, case_hand))
    whowins(player_hand, case_hand, dest, bet)
    
def whowins(player_hand, case_hand, dest, bet): 
    player_score = handscore(player_hand, dest)
    case_score = handscore(case_hand, dest)
    if player_score > case_score: playerwins(bet)
    elif player_score == case_score: tie(bet)
    else: casewins(bet)

def tie(bet):
    return print("Tie, you won {}".format(bet))
    exit()

def shouldcasedrawcard(player_hand, case_hand, dest):
    if handscore(case_hand, dest) < 17: return True
    return False

def isitover21(hand, dest): #A  1 or 11
    if handscore(hand, dest) > 21:
        return True
    return False

def handscore(hand, dest):
    score = 0
    for card in hand:
        score += dest[card][0]
    if score > 21 and "A" in hand: score -= 10
    return score

def drawcard(cards, dest):
    card = choice(cards)
    if dest[card][1] > 0:
        dest[card][1] -= 1
        return card
    else: 
       return drawcard(hand, cards, dest)
    
def doyouwanttodraw():
    task = input("Do you want to draw a card.")
    if task.lower()[0] == "y":
        return True
    return False

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

