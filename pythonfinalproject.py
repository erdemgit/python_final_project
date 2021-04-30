from random import choice

def main():
    app_flow()

def app_flow():
    """balance = int(input("How much money you want to invest: "))
    bet = int(input("How much you want to bet: "))
    balance -= bet"""
    game()
    
def game():
    deck = {
        "A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10
    }
    deck_string = "A2345678910JQK"
    player_hand = choice(deck_string) + choice(deck_string)
    if isitbj(player_hand):
        print("blackjack")
        print("{}: {}".format(player_hand, handscore(deck, player_hand)))
    print(handscore(deck, player_hand))
    case_hand = choice(deck_string) + choice(deck_string)
    if isitbj(case_hand):
        print("blackjack")
        print("{}: {}".format(case_hand, handscore(deck, case_hand)))
    print(handscore(deck, case_hand))
    task = input("Do you want to draw card: ")

    
    
def isitbj(hand):
    if "A" in hand:
        for card in "JQK":
            if card in hand:
                return True
    return False

def handscore(deck, hand):
    score = 0
    for card in hand:
        score += deck[card]
    return score

def player_wonned()        
    

main()
