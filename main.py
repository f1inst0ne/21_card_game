#My own Blackjack version of Game
#Сделано оно для себя, в учебных целях
#Дабы научится рабоать с Git и попрактиковать python

import random

def player_take_card():
    take_card = random.randint(1, 11)
    player_cur_cards.append(take_card)
    take_index = all_cards.index(take_card)
    all_cards.pop(take_index)
    return player_cur_cards, all_cards


all_cards = []


#Making full card deck
for i in range(1, 10):
    for j in range(4):
        all_cards.append(i)
for i in range(16):
    all_cards.append(10)
for i in range(4):
    all_cards.append(11)


croupier_cur_cards = []
player_cur_cards = []

#Croupier takes two cards
for i in range(2):
    take_card = random.randint(1, 11)
    croupier_cur_cards.append(take_card)
    take_index = all_cards.index(take_card)
    all_cards.pop(take_index)


#Player takes two cards
for i in range(2):
    take_card = random.randint(1, 11)
    player_cur_cards.append(take_card)
    take_index = all_cards.index(take_card)
    all_cards.pop(take_index)
print('Crup cards:', croupier_cur_cards)
print('Player cards:', player_cur_cards)
print(all_cards)
