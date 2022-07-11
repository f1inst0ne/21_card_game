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

def croupier_take_card():
    take_card = random.randint(1, 11)
    croupier_cur_cards.append(take_card)
    take_index = all_cards.index(take_card)
    all_cards.pop(take_index)
    return croupier_cur_cards, all_cards
def check_winner():
    return sum(player_cur_cards) > sum(croupier_cur_cards)


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
while sum(player_cur_cards) <= 21:
    print(croupier_cur_cards[0], '#')
    print(player_cur_cards)
    print('What do you want to do?:')
    print('You can:')
    print('1) Hit')
    print('2) Stand')
    print('3) Double down')
    user_input = input('>>>')
    if user_input == '1':
        player_take_card()
    elif user_input == '2':
        print(check_winner())
        break
    elif user_input == '3':
        player_take_card()
        print(check_winner())
        break
print(croupier_cur_cards)
print(player_cur_cards)

