#tasowanie kart
colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']
allCards = []

for color in colors:
    for figure in figures:
        card = figure + ' ' + color
        allCards.append(card)
print(allCards)

import random
random.shuffle(allCards)
print(allCards)
player1 = []
player2 = []

max=len(allCards)
for i in range(max):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
        
print(player1)
print(player2)
