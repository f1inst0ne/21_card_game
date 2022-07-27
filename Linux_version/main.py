#My own Blackjack version of Game
#Сделано оно для себя, в учебных целях
#Дабы научится рабоать с Git и попрактиковать python
import os
import random
os.system('clear')


#Добор карты игроком
def player_take_card():
    take_card = random.randint(2, 11)
    player_cur_cards.append(take_card)
    take_index = all_cards.index(take_card)
    all_cards.pop(take_index)
    return player_cur_cards, all_cards


#Добор карты крупье
def croupier_take_card():
    take_card = random.randint(2, 11)
    croupier_cur_cards.append(take_card)
    take_index = all_cards.index(take_card)
    all_cards.pop(take_index)
    return croupier_cur_cards, all_cards


#Проверка победителя между игроком и диллером
def check_winner():
    os.system('clear')
    if sum(player_cur_cards) > sum(croupier_cur_cards):
        return 'You are the winner!!!!!!!!!!!!'
    elif sum(player_cur_cards) == sum(croupier_cur_cards):
        return 'It is draw-_-'
    else:
        return 'You are looooser(((((((('


def croupier_card_check():
    need_cards = 0
    need_chance = 25
    cards_to_check = 21 - sum(croupier_cur_cards)
    for i in range(2, cards_to_check + 1):
        if i > 11:
            break
        else:
            need_cards += all_cards.count(i)
    return need_cards / len(all_cards) * 100 >= need_chance


all_cards = []

#Making full card deck
for i in range(2, 10):
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
    take_card = random.randint(2, 11)
    croupier_cur_cards.append(take_card)
    take_index = all_cards.index(take_card)
    all_cards.pop(take_index)


#Player takes two cards
for i in range(2):
    take_card = random.randint(2, 11)
    player_cur_cards.append(take_card)
    take_index = all_cards.index(take_card)
    all_cards.pop(take_index)
while sum(player_cur_cards) <= 21:
    if len(player_cur_cards) == 2:
        print(croupier_cur_cards[0], '#')
        print(player_cur_cards)
        print('What do you want to do?:')
        print('You can:')
        print('1) Hit')
        print('2) Stand')
        print('3) Double down')
    else:
        print(croupier_cur_cards[0], '#')
        print(player_cur_cards)
        print('What do you want to do?:')
        print('You can:')
        print('1) Hit')
        print('2) Stand') 
    user_input = input('>>>')
    if user_input == '1':
        player_take_card()
        os.system('clear')
    elif user_input == '2':
        os.system('clear')
        break
    elif user_input == '3' and len(player_cur_cards) == 2:
        os.system('clear')
        player_take_card()
        break
    else:
        os.system('clear')
        print('Invaild command!Try again!!!!')
while croupier_card_check():
    croupier_take_card()
if sum(player_cur_cards) > 21 and sum(croupier_cur_cards) <= 21:
    print('You have lost((((((')
elif sum(croupier_cur_cards) > 21 and sum(player_cur_cards) <= 21:
    print('You have won!!!!!!!')
else:
    print(check_winner())
print('Croupier had:', croupier_cur_cards, 'His sum:', sum(croupier_cur_cards))
print('Player had:', player_cur_cards, 'Your sum:', sum(player_cur_cards))
exit_input = input('Press any ENTER to exit....')
os.system('clear')

