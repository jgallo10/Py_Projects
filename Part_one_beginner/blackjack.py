#simple blackjack game
 
import random
 
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calcualte_score(cards):
    score = sum(cards)
    if score == 21:
        return 0
    elif score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return score
        
        
def blackjack():
    win = 21
    player = []
    dealer = []
    
    for card in range(2):
        player.append(deal_card())
        dealer.append(deal_card())
    
    player_score = calcualte_score(player)
    dealer_score = calcualte_score(dealer)
    
    if player_score == 0:
        print(f"")
        
   
   
        
        
blackjack()