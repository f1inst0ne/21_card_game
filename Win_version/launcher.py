import os
os.system('title Blackjack')
os.system('cls')
flag = True
while flag: 
    print(' ______________________\n/            ___       \\ \n|   |   /\\  /   | /    | \n|   |  /__\\ |    |<     | \n| __| /    \\\\___ | \\    | \n|                       | \n|     _____  _____      | \n|    /$$$$$\\/$$$$$\\     | \n|    \\$$$$$$$$$$$$/     | \n|     \\$$$$$$$$$$/      | \n|      \\$$$$$$$$/       | \n|       \\$$$$$$/        | \n|        \\$$$$/         | \n|         \\$$/          | \n|          \\/           | \n|                       | \n|  $$$$$$$$$$$$$$$$$$$  | \n\\_______________________/ \n')
    print('Welcome to blackjack game')
    print('What do you want to do?')
    print('1)Play \n2)Exit')
    user_input = input('>>>')
    if user_input == '1':
        os.system('python main.py')
    elif user_input == '2':
        flag = False
    else:
        print('invaild command!!!!!! Try again!')
os.system('cls')
