import random
import math
import time

# Introduction

print("""The COVID-19 pandemic has caused severe damage around the world.
We are fighting for life with very few humane vaccines left.
The three of you are in the vulnerable group and need to be prioritized, but now we only have 2 doses left.
So we have to choose the 2 smartest and bravest out of the 3 of you to give these two precious vaccines.
To be able to be vaccinated, you will have to go through 4 rounds of our game to choose the 2 most deserving people.
""")
time.sleep(2.5)

# Game 1
print('''
 _    _ _   _  _____ _____ _        ___________   ______ ___________ _____ _   _ _   _  _____ 
| |  | | | | ||  ___|  ___| |      |  _  |  ___|  |  ___|  _  | ___ \_   _| | | | \ | ||  ___|
| |  | | |_| || |__ | |__ | |      | | | | |_     | |_  | | | | |_/ / | | | | | |  \| || |__  
| |/\| |  _  ||  __||  __|| |      | | | |  _|    |  _| | | | |    /  | | | | | | . ` ||  __| 
\  /\  / | | || |___| |___| |____  \ \_/ / |      | |   \ \_/ / |\ \  | | | |_| | |\  || |___ 
 \/  \/\_| |_/\____/\____/\_____/   \___/\_|      \_|    \___/\_| \_| \_/  \___/\_| \_/\____/''')  # Title of the game

amounts = [100, 200, 300, 400, 500, 'double', 'half', 'lose turn', 'spin again']

topic = 'Name of the ancient animal'
phrase = "dinosaur".upper()  # the word to be guessed by the players
# each player will take a turn to spin the wheel then will have to guess the letter that contains in the phrase,
# right answers will get the point and wrong will have nothing or will take a penalty
total = 0
Word = []
for char in phrase:
    if char.isalpha():
        Word.append('_')
    else:
        Word.append(char)


def print_word(phrase):
    for char in phrase:
        print(char, end=' ')
    print()


# replace each character in the phrase with underscores

print('The topic is: ' + topic)
print('The phrase is:')
print_word(Word)
player1 = input('Enter your name here: ')
player2 = input('Enter your name here: ')
player3 = input('Enter your name here: ')

total = 0


# spin the wheel
def spin_wheel():
    spin = random.choice(amounts)
    return spin


p1 = "p1_move"
p2 = "p2_move"
p3 = "p3_move"

p1_move = 0
p2_move = 0
p3_move = 0

# 4 following lines are to return the string with the guessed letter at every round
guessed = "_" * len(phrase)
phrase = list(phrase)
guessed = list(guessed)
lstGuessed = []

player_dict = {'p1': 0, 'p2': 0, 'p3': 0}  # a dict to store player's score
while True:  # keep playing until the phrase is guessed
    if '_' in guessed:
        while True:
            # PLAYER1
            # If 1 player guesses the correct letter in the word, the turn will still belong to the next player to
            # ensure balance for the game.
            p1_move = spin_wheel()
            print("Player 1 spun for", p1_move)
            if p1_move == 'lose turn':  # skip player turn
                pass
            elif p1_move == 'spin again':  # player have to spin again and the procedure is the same with the main one
                p1_move = spin_wheel()
                print("Player 1 spun for", p1_move)
                if p1_move == 'lose turn':
                    pass
                elif p1_move == 'spin again':  # the game will break if the player receive 'spin again' more than once
                    print('congratulation! you break the game with your lucky')
                    all_values = player_dict.values()
                    max_value = max(all_values)
                    min_value = min(all_values)
                    if max_value == player_dict['p1']:  # find out who has the highest score
                        winner1 = player1
                        print('winner1 is player1')
                    elif max_value == player_dict['p2']:  # find out who has the highest score
                        winner1 = player2
                        print('winner1 is player2')
                    elif max_value == player_dict['p3']:  # find out who has the highest score
                        winner1 = player3
                        print('winner1 is player3')
                    if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                        winner2 = player1
                        print('winner2 is player1')
                    elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                        winner2 = player2
                        print('winner2 is player2')
                    elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                        winner2 = player3
                        print('winner2 is player2')
                    print(player_dict)
                    print('two players who have the highest score win the game')
                    break
                else:
                    p1_answer = input("Player 1, enter your answer here:  ").upper()  # answer of p1
                    print(player1 + ' ' + 'guessed' + ' ' + p1_answer)  # print the answer
                    new_string = phrase.count(p1_answer)  # count the number of letter in phrase
                    if p1_answer == 'dinosaur'.upper():  # player can guess the whole word at any time they want
                        print('congratulation! you guess the whole phrase')
                        player_dict['p1'] = player_dict['p1'] + 1000
                        all_values = player_dict.values()
                        max_value = max(all_values)
                        min_value = min(all_values)
                        if max_value == player_dict['p1']:  # find out who has the highest score
                            winner1 = player1
                            print('winner1 is player1')
                        elif max_value == player_dict['p2']:  # find out who has the highest score
                            winner1 = player2
                            print('winner1 is player2')
                        elif max_value == player_dict['p3']:  # find out who has the highest score
                            winner1 = player3
                            print('winner1 is player3')
                        if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                            winner2 = player1
                            print('winner2 is player1')
                        elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                            winner2 = player2
                            print('winner2 is player2')
                        elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                            winner2 = player3
                            print('winner2 is player2')
                        print(player_dict)
                        print('two players who have the highest score win the game')
                        break
                    else:
                        if p1_answer in phrase and p1_answer not in guessed:
                            for i in range(2):  # loop to return the string
                                if p1_answer in phrase:
                                    index = phrase.index(p1_answer)
                                    guessed[index] = p1_answer  # the order of the guessed letter in the word
                                    phrase[index] = '_'  # replace it with underscores
                                else:
                                    print(''.join(guessed))
                                    if p1_answer != '':
                                        lstGuessed.append(p1_answer)  # fill in the guessed list
                                if '_' not in guessed:
                                    print('correct')
                            print('current guessed list is: ', lstGuessed)
                            if p1_move == 'double':
                                player_dict['p1'] = player_dict['p1'] * 2  # double the score
                                print('p1 points: ', player_dict['p1'])
                            elif p1_move == 'half':  # nothing will happen if they guess it right
                                player_dict['p1'] = player_dict['p1']
                                print('p1 points: ', player_dict['p1'])
                            elif p1_move == 'lose turn':
                                pass
                            else:
                                player_dict['p1'] += (p1_move * int(new_string))
                                print('p1 points: ', player_dict['p1'])
                            continue
                            if '_' in guessed:
                                continue
                            else:
                                break
                        else:  # if the player get it wrong
                            lstGuessed.append(p1_answer)  # fill the answer into the list with guessed letters
                            print('current guessed list is: ', lstGuessed)
                            if p1_move == 'half':  # divide by 2 if the answer is wrong
                                player_dict['p1'] = math.ceil(player_dict['p1'] / 2)
                                print('your answer is not correct or they are already guessed')
                                print('p1 points: ', player_dict['p1'])
                            else:
                                player_dict['p1'] = player_dict['p1']
                                print('p1 points: ', player_dict['p1'])
                                print('your answer is not correct or they are already guessed')
                            pass
                    if '_' not in guessed:
                        all_values = player_dict.values()
                        max_value = max(all_values)
                        min_value = min(all_values)
                        if max_value == player_dict['p1']:  # find out who has the highest score
                            winner1 = player1
                            print('winner1 is player1')
                        elif max_value == player_dict['p2']:  # find out who has the highest score
                            winner1 = player2
                            print('winner1 is player2')
                        elif max_value == player_dict['p3']:  # find out who has the highest score
                            winner1 = player3
                            print('winner1 is player3')
                        if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                            winner2 = player1
                            print('winner2 is player1')
                        elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                            winner2 = player2
                            print('winner2 is player2')
                        elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                            winner2 = player3
                            print('winner2 is player2')
                        print(player_dict)
                        print('two players who have the highest score win the game')
                        break

            else:
                p1_answer = input("Player 1, enter your answer here:  ").upper()  # answer of p1
                print(player1 + ' ' + 'guessed' + ' ' + p1_answer)  # print the answer
                new_string = phrase.count(p1_answer)  # count the number of letter in phrase
                if p1_answer == 'dinosaur'.upper():  # if the player can guess the whole phrase
                    print('congratulation! you guess the whole phrase')
                    player_dict['p1'] = player_dict['p1'] + 1000  # return the value for the next game
                    all_values = player_dict.values()
                    max_value = max(all_values)
                    min_value = min(all_values)
                    if max_value == player_dict['p1']:  # find out who has the highest score
                        winner1 = player1
                        print('winner1 is player1')
                    elif max_value == player_dict['p2']:  # find out who has the highest score
                        winner1 = player2
                        print('winner1 is player2')
                    elif max_value == player_dict['p3']:  # find out who has the highest score
                        winner1 = player3
                        print('winner1 is player3')
                    if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                        winner2 = player1
                        print('winner2 is player1')
                    elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                        winner2 = player2
                        print('winner2 is player2')
                    elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                        winner2 = player3
                        print('winner2 is player2')
                    print(player_dict)
                    print('two players who have the highest score win the game')
                    break
                else:
                    if p1_answer in phrase and p1_answer not in guessed:  # if the player guess the wrong character
                        for i in range(2):  # loop to return the string
                            if p1_answer in phrase:  # index the character
                                index = phrase.index(p1_answer)
                                guessed[index] = p1_answer
                                phrase[index] = '_'
                            else:
                                print(''.join(guessed))
                                if p1_answer != '':
                                    lstGuessed.append(p1_answer)  # append to the guessed list
                            if '_' not in guessed:
                                print('correct')
                        print('current guessed list is: ', lstGuessed)
                        if p1_move == 'double':
                            player_dict['p1'] = player_dict['p1'] * 2  # double the score
                            print('p1 points: ', player_dict['p1'])
                        elif p1_move == 'half':  # nothing will happen if they guess it right
                            player_dict['p1'] = player_dict['p1']
                            print('p1 points: ', player_dict['p1'])
                        elif p1_move == 'lose turn':
                            pass
                        else:
                            player_dict['p1'] += (p1_move * int(new_string))
                            print('p1 points: ', player_dict['p1'])
                        if '_' in guessed:
                            continue
                        else:
                            all_values = player_dict.values()
                            max_value = max(all_values)
                            min_value = min(all_values)
                            if max_value == player_dict['p1']:  # find out who has the highest score
                                winner1 = player1
                                print('winner1 is player1')
                            elif max_value == player_dict['p2']:  # find out who has the highest score
                                winner1 = player2
                                print('winner1 is player2')
                            elif max_value == player_dict['p3']:  # find out who has the highest score
                                winner1 = player3
                                print('winner1 is player3')
                            if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                                winner2 = player1
                                print('winner2 is player1')
                            elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                                winner2 = player2
                                print('winner2 is player2')
                            elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                                winner2 = player3
                                print('winner2 is player2')
                            print(player_dict)
                            print('two players who have the highest score win the game')
                            break
                    else:
                        lstGuessed.append(p1_answer)
                        print('current guessed list is: ', lstGuessed)
                        if p1_move == 'half':  # divide by 2 if the answer is wrong
                            player_dict['p1'] = math.ceil(player_dict['p1'] / 2)
                            print('your answer is not correct or they are already guessed')
                            print('p1 points: ', player_dict['p1'])
                        else:
                            player_dict['p1'] = player_dict['p1']  # they guessed it wrong but nothing is taken as
                            # penalty
                            print('p1 points: ', player_dict['p1'])
                            print('your answer is not correct or they are already guessed')
                        break
    else:
        break

    # The code is basically the same as above, just change the name of each player
    # PLAYER2
    # If 1 player guesses the correct letter in the word, the turn will still belong to the next player to
    # ensure balance for the game.
    if '_' in guessed:
        while True:
            p2_move = spin_wheel()
            print("Player 2 spun for", p2_move)
            if p2_move == 'lose turn':
                break
            elif p2_move == 'spin again':
                p2_move = spin_wheel()
                print("Player 2 spun for", p2_move)
                if p2_move == 'lose turn':
                    break
                elif p2_move == 'spin again':
                    print('congratulation! you break the game with your lucky')
                    all_values = player_dict.values()
                    max_value = max(all_values)
                    min_value = min(all_values)
                    if max_value == player_dict['p1']:  # find out who has the highest score
                        winner1 = player1
                        print('winner1 is player1')
                    elif max_value == player_dict['p2']:  # find out who has the highest score
                        winner1 = player2
                        print('winner1 is player2')
                    elif max_value == player_dict['p3']:  # find out who has the highest score
                        winner1 = player3
                        print('winner1 is player3')
                    if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                        winner2 = player1
                        print('winner2 is player1')
                    elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                        winner2 = player2
                        print('winner2 is player2')
                    elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                        winner2 = player3
                        print('winner2 is player2')
                    print(player_dict)
                    print('two players who have the highest score win the game')
                    break
                else:
                    p2_answer = input("Player 2, enter your answer here:  ").upper()
                    print(player2 + ' ' + 'guessed' + ' ' + p2_answer)
                    new_string = phrase.count(p2_answer)
                    if p2_answer == 'dinosaur'.upper():
                        print('congratulation! you guess the whole phrase')
                        player_dict['p2'] = player_dict['p2'] + 1000
                        all_values = player_dict.values()
                        max_value = max(all_values)
                        min_value = min(all_values)
                        if max_value == player_dict['p1']:  # find out who has the highest score
                            winner1 = player1
                            print('winner1 is player1')
                        elif max_value == player_dict['p2']:  # find out who has the highest score
                            winner1 = player2
                            print('winner1 is player2')
                        elif max_value == player_dict['p3']:  # find out who has the highest score
                            winner1 = player3
                            print('winner1 is player3')
                        if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                            winner2 = player1
                            print('winner2 is player1')
                        elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                            winner2 = player2
                            print('winner2 is player2')
                        elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                            winner2 = player3
                            print('winner2 is player2')
                        print(player_dict)
                        print('two players who have the highest score win the game')
                        break
                    else:
                        if p2_answer in phrase and p2_answer not in guessed:
                            for i in range(2):
                                if p2_answer in phrase:
                                    index = phrase.index(p2_answer)
                                    guessed[index] = p2_answer
                                    phrase[index] = '_'
                                else:
                                    print(''.join(guessed))
                                    if p2_answer != '':
                                        lstGuessed.append(p2_answer)
                                if '_' not in guessed:
                                    print('correct')
                            print('current guessed list is: ', lstGuessed)
                            if p2_move == 'double':
                                player_dict['p2'] = player_dict['p2'] * 2
                                print('p2 points: ', player_dict['p2'])
                            elif p2_move == 'half':
                                player_dict['p2'] = player_dict['p2']
                                print('p2 points: ', player_dict['p2'])
                            elif p2_move == 'lose turn':
                                break
                            else:
                                player_dict['p2'] += (p2_move * int(new_string))
                                print('p2 points: ', player_dict['p2'])
                            if '_' in guessed:
                                continue
                            else:
                                all_values = player_dict.values()
                                max_value = max(all_values)
                                min_value = min(all_values)
                                if max_value == player_dict['p1']:  # find out who has the highest score
                                    winner1 = player1
                                    print('winner1 is player1')
                                elif max_value == player_dict['p2']:  # find out who has the highest score
                                    winner1 = player2
                                    print('winner1 is player2')
                                elif max_value == player_dict['p3']:  # find out who has the highest score
                                    winner1 = player3
                                    print('winner1 is player3')
                                if max_value > player_dict['p1'] > min_value:  # find out who has the second highest
                                    # score
                                    winner2 = player1
                                    print('winner2 is player1')
                                elif max_value > player_dict['p2'] > min_value:  # find out who has the second
                                    # highest score
                                    winner2 = player2
                                    print('winner2 is player2')
                                elif max_value > player_dict['p3'] > min_value:  # find out who has the second
                                    # highest score
                                    winner2 = player3
                                    print('winner2 is player2')
                                print(player_dict)
                                print('two players who have the highest score win the game')
                                break

                        else:
                            lstGuessed.append(p2_answer)
                            print('current guessed list is: ', lstGuessed)
                            if p2_move == 'half':
                                player_dict['p2'] = math.ceil(player_dict['p2'] / 2)
                                print('p2 points: ', player_dict['p2'])
                            else:
                                player_dict['p2'] = player_dict['p2']
                                print('p2 points: ', player_dict['p2'])
                                print('your answer is not correct or they are already guessed')
                                break
                        if '_' not in guessed:
                            all_values = player_dict.values()
                            max_value = max(all_values)
                            min_value = min(all_values)
                            if max_value == player_dict['p1']:  # find out who has the highest score
                                winner1 = player1
                                print('winner1 is player1')
                            elif max_value == player_dict['p2']:  # find out who has the highest score
                                winner1 = player2
                                print('winner1 is player2')
                            elif max_value == player_dict['p3']:  # find out who has the highest score
                                winner1 = player3
                                print('winner1 is player3')
                            if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                                winner2 = player1
                                print('winner2 is player1')
                            elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                                winner2 = player2
                                print('winner2 is player2')
                            elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                                winner2 = player3
                                print('winner2 is player2')
                            print(player_dict)
                            print('two players who have the highest score win the game')
                            break

            else:
                p2_answer = input("Player 2, enter your answer here:  ").upper()
                print(player2 + ' ' + 'guessed' + ' ' + p2_answer)
                new_string = phrase.count(p2_answer)
                if p2_answer == 'dinosaur'.upper():
                    print('congratulation! you guess the whole phrase')
                    player_dict['p2'] = player_dict['p2'] + 1000
                    all_values = player_dict.values()
                    max_value = max(all_values)
                    min_value = min(all_values)
                    if max_value == player_dict['p1']:  # find out who has the highest score
                        winner1 = player1
                        print('winner1 is player1')
                    elif max_value == player_dict['p2']:  # find out who has the highest score
                        winner1 = player2
                        print('winner1 is player2')
                    elif max_value == player_dict['p3']:  # find out who has the highest score
                        winner1 = player3
                        print('winner1 is player3')
                    if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                        winner2 = player1
                        print('winner2 is player1')
                    elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                        winner2 = player2
                        print('winner2 is player2')
                    elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                        winner2 = player3
                        print('winner2 is player2')
                    print(player_dict)
                    print('two players who have the highest score win the game')
                    break
                else:
                    if p2_answer in phrase and p2_answer not in guessed:
                        for i in range(2):
                            if p2_answer in phrase:
                                index = phrase.index(p2_answer)
                                guessed[index] = p2_answer
                                phrase[index] = '_'
                            else:
                                print(''.join(guessed))
                                if p2_answer != '':
                                    lstGuessed.append(p2_answer)
                            if '_' not in guessed:
                                print('correct')
                        print('current guessed list is: ', lstGuessed)
                        if p2_move == 'double':
                            player_dict['p2'] = player_dict['p2'] * 2
                            print('p2 points: ', player_dict['p2'])
                        elif p2_move == 'half':
                            player_dict['p2'] = player_dict['p2']
                            print('p2 points: ', player_dict['p2'])
                        elif p2_move == 'lose turn':
                            break
                        else:
                            player_dict['p2'] += (p2_move * int(new_string))
                            print('p2 points: ', player_dict['p2'])
                        if '_' in guessed:
                            continue
                        else:
                            all_values = player_dict.values()
                            max_value = max(all_values)
                            min_value = min(all_values)
                            if max_value == player_dict['p1']:  # find out who has the highest score
                                winner1 = player1
                                print('winner1 is player1')
                            elif max_value == player_dict['p2']:  # find out who has the highest score
                                winner1 = player2
                                print('winner1 is player2')
                            elif max_value == player_dict['p3']:  # find out who has the highest score
                                winner1 = player3
                                print('winner1 is player3')
                            if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                                winner2 = player1
                                print('winner2 is player1')
                            elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                                winner2 = player2
                                print('winner2 is player2')
                            elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                                winner2 = player3
                                print('winner2 is player2')
                            print(player_dict)
                            print('two players who have the highest score win the game')
                            break

                    else:
                        lstGuessed.append(p2_answer)
                        print('current guessed list is: ', lstGuessed)
                        if p2_move == 'half':
                            player_dict['p2'] = math.ceil(player_dict['p2'] / 2)
                            print('p2 points: ', player_dict['p2'])
                        else:
                            player_dict['p2'] = player_dict['p2']
                            print('p2 points: ', player_dict['p2'])
                            print('your answer is not correct or they are already guessed')
                            break
    else:
        break

    if '_' in guessed:
        while True:
            # PLAYER3
            # If 1 player guesses the correct letter in the word, the turn will still belong to the next player to
            # ensure balance for the game.
            p3_move = spin_wheel()
            print("Player 3 spun for", p3_move)
            if p3_move == 'lose turn':
                break
            elif p3_move == 'spin again':
                p3_move = spin_wheel()
                print("Player 3 spun for", p3_move)
                if p3_move == 'lose turn':
                    break
                elif p3_move == 'spin again':
                    print('congratulation! you break the game with your lucky')
                    all_values = player_dict.values()
                    max_value = max(all_values)
                    min_value = min(all_values)
                    if max_value == player_dict['p1']:  # find out who has the highest score
                        winner1 = player1
                        print('winner1 is player1')
                    elif max_value == player_dict['p2']:  # find out who has the highest score
                        winner1 = player2
                        print('winner1 is player2')
                    elif max_value == player_dict['p3']:  # find out who has the highest score
                        winner1 = player3
                        print('winner1 is player3')
                    if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                        winner2 = player1
                        print('winner2 is player1')
                    elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                        winner2 = player2
                        print('winner2 is player2')
                    elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                        winner2 = player3
                        print('winner2 is player2')
                    print(player_dict)
                    print('two players who have the highest score win the game')
                    break
                else:
                    p3_answer = input("Player 3, enter your answer here:  ").upper()
                    print(player3 + ' ' + 'guessed' + ' ' + p3_answer)
                    new_string = phrase.count(p3_answer)
                    if p3_answer == 'dinosaur'.upper():
                        print('congratulation! you guess the whole phrase')
                        player_dict['p3'] = player_dict['p3'] + 1000
                        all_values = player_dict.values()
                        max_value = max(all_values)
                        min_value = min(all_values)
                        if max_value == player_dict['p1']:  # find out who has the highest score
                            winner1 = player1
                            print('winner1 is player1')
                        elif max_value == player_dict['p2']:  # find out who has the highest score
                            winner1 = player2
                            print('winner1 is player2')
                        elif max_value == player_dict['p3']:  # find out who has the highest score
                            winner1 = player3
                            print('winner1 is player3')
                        if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                            winner2 = player1
                            print('winner2 is player1')
                        elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                            winner2 = player2
                            print('winner2 is player2')
                        elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                            winner2 = player3
                            print('winner2 is player2')
                        print(player_dict)
                        print('two players who have the highest score win the game')
                        break
                    else:
                        if p3_answer in phrase and p3_answer not in guessed:
                            for i in range(2):
                                if p3_answer in phrase:
                                    index = phrase.index(p3_answer)
                                    guessed[index] = p3_answer
                                    phrase[index] = '_'
                                else:
                                    print(''.join(guessed))
                                    if p3_answer != '':
                                        lstGuessed.append(p3_answer)
                                if '_' not in guessed:
                                    print('correct')
                            print('current guessed list is: ', lstGuessed)
                            if p3_move == 'double':
                                player_dict['p3'] = player_dict['p3'] * 2
                                print('p3 points: ', player_dict['p3'])
                            elif p3_move == 'half':
                                player_dict['p3'] = player_dict['p3']
                                print('p3 points: ', player_dict['p3'])
                            elif p3_move == 'lose turn':
                                break
                            else:
                                player_dict['p3'] += (p3_move * int(new_string))
                                print('p3 points: ', player_dict['p3'])
                            if '_' in guessed:
                                continue
                            else:
                                all_values = player_dict.values()
                                max_value = max(all_values)
                                min_value = min(all_values)
                                if max_value == player_dict['p1']:  # find out who has the highest score
                                    winner1 = player1
                                    print('winner1 is player1')
                                elif max_value == player_dict['p2']:  # find out who has the highest score
                                    winner1 = player2
                                    print('winner1 is player2')
                                elif max_value == player_dict['p3']:  # find out who has the highest score
                                    winner1 = player3
                                    print('winner1 is player3')
                                if max_value > player_dict['p1'] > min_value:  # find out who has the second highest
                                    # score
                                    winner2 = player1
                                    print('winner2 is player1')
                                elif max_value > player_dict['p2'] > min_value:  # find out who has the second
                                    # highest score
                                    winner2 = player2
                                    print('winner2 is player2')
                                elif max_value > player_dict['p3'] > min_value:  # find out who has the second
                                    # highest score
                                    winner2 = player3
                                    print('winner2 is player2')
                                print(player_dict)
                                print('two players who have the highest score win the game')
                                break
                        if '_' not in guessed:
                            print(player_dict)
                            all_values = player_dict.values()
                            max_value = max(all_values)
                            min_value = min(all_values)
                            if max_value == player_dict['p1']:  # find out who has the highest score
                                winner1 = player1
                                print('winner1 is player1')
                            elif max_value == player_dict['p2']:  # find out who has the highest score
                                winner1 = player2
                                print('winner1 is player2')
                            elif max_value == player_dict['p3']:  # find out who has the highest score
                                winner1 = player3
                                print('winner1 is player3')
                            if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                                winner2 = player1
                                print('winner2 is player1')
                            elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                                winner2 = player2
                                print('winner2 is player2')
                            elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                                winner2 = player3
                                print('winner2 is player2')
                            print(player_dict)
                            print('two players who have the highest score win the game')
                            break

                        else:
                            lstGuessed.append(p3_answer)
                            print('current guessed list is: ', lstGuessed)
                            if p3_move == 'half':
                                player_dict['p3'] = math.ceil(player_dict['p3'] / 2)
                                print('p3 points: ', player_dict['p3'])
                            else:
                                player_dict['p3'] = player_dict['p3']
                                print('p3 points: ', player_dict['p3'])
                                print('your answer is not correct or they are already guessed')
                                break
                if '_' not in guessed:
                    print(player_dict)
                    all_values = player_dict.values()
                    max_value = max(all_values)
                    min_value = min(all_values)
                    if max_value == player_dict['p1']:  # find out who has the highest score
                        winner1 = player1
                        print('winner1 is player1')
                    elif max_value == player_dict['p2']:  # find out who has the highest score
                        winner1 = player2
                        print('winner1 is player2')
                    elif max_value == player_dict['p3']:  # find out who has the highest score
                        winner1 = player3
                        print('winner1 is player3')
                    if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                        winner2 = player1
                        print('winner2 is player1')
                    elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                        winner2 = player2
                        print('winner2 is player2')
                    elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                        winner2 = player3
                        print('winner2 is player2')
                    print(player_dict)
                    print('two players who have the highest score win the game')
                    break
            else:
                p3_answer = input("Player 3, enter your answer here:  ").upper()
                print(player3 + ' ' + 'guessed' + ' ' + p3_answer)
                new_string = phrase.count(p3_answer)
                if p3_answer == 'dinosaur'.upper():
                    print('congratulation! you guess the whole phrase')
                    player_dict['p3'] = player_dict['p3'] + 1000
                    all_values = player_dict.values()
                    max_value = max(all_values)
                    min_value = min(all_values)
                    if max_value == player_dict['p1']:  # find out who has the highest score
                        winner1 = player1
                        print('winner1 is player1')
                    elif max_value == player_dict['p2']:  # find out who has the highest score
                        winner1 = player2
                        print('winner1 is player2')
                    elif max_value == player_dict['p3']:  # find out who has the highest score
                        winner1 = player3
                        print('winner1 is player3')
                    if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                        winner2 = player1
                        print('winner2 is player1')
                    elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                        winner2 = player2
                        print('winner2 is player2')
                    elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                        winner2 = player3
                        print('winner2 is player2')
                    print(player_dict)
                    print('two players who have the highest score win the game')
                    break
                else:
                    if p3_answer in phrase and p3_answer not in guessed:
                        for i in range(2):
                            if p3_answer in phrase:
                                index = phrase.index(p3_answer)
                                guessed[index] = p3_answer
                                phrase[index] = '_'
                            else:
                                print(''.join(guessed))
                                if p3_answer != '':
                                    lstGuessed.append(p3_answer)
                            if '_' not in guessed:
                                print('correct')
                        print('current guessed list is: ', lstGuessed)
                        if p3_move == 'double':
                            player_dict['p3'] = player_dict['p3'] * 2
                            print('p3 points: ', player_dict['p3'])
                        elif p3_move == 'half':
                            player_dict['p3'] = player_dict['p3']
                            print('p3 points: ', player_dict['p3'])
                        elif p3_move == 'lose turn':
                            break
                        else:
                            player_dict['p3'] += (p3_move * int(new_string))
                            print('p3 points: ', player_dict['p3'])
                        if '_' in guessed:
                            continue
                        else:
                            all_values = player_dict.values()
                            max_value = max(all_values)
                            min_value = min(all_values)
                            if max_value == player_dict['p1']:  # find out who has the highest score
                                winner1 = player1
                                print('winner1 is player1')
                            elif max_value == player_dict['p2']:  # find out who has the highest score
                                winner1 = player2
                                print('winner1 is player2')
                            elif max_value == player_dict['p3']:  # find out who has the highest score
                                winner1 = player3
                                print('winner1 is player3')
                            if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                                winner2 = player1
                                print('winner2 is player1')
                            elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                                winner2 = player2
                                print('winner2 is player2')
                            elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                                winner2 = player3
                                print('winner2 is player2')
                            print(player_dict)
                            print('two players who have the highest score win the game')
                            break
                    else:
                        lstGuessed.append(p3_answer)
                        print('current guessed list is: ', lstGuessed)
                        if p3_move == 'half':
                            player_dict['p3'] = math.ceil(player_dict['p3'] / 2)
                            print('p3 points: ', player_dict['p3'])
                        else:
                            player_dict['p3'] = player_dict['p3']
                            print('p3 points: ', player_dict['p3'])
                            print('your answer is not correct or they are already guessed')
                        break
    else:
        break

# ROUND 2


print('round 2 begin: ')

topic = 'It is a noun'
phrase = "bankruptcy".upper()
Word = []
for char in phrase:
    if char.isalpha():
        Word.append('_')
    else:
        Word.append(char)


def print_word(phrase):
    for char in phrase:
        print(char, end=' ')
    print()


# replace each character in the phrase with underscores

print('The topic is: ' + topic)
print('The phrase is:')
print_word(Word)

# 4 following lines are to return the string with the guessed letter at every round
guessed = "_" * len(phrase)
phrase = list(phrase)
guessed = list(guessed)
lstGuessed = []
while True:  # keep playing until the phrase is guessed
    if '_' in guessed:
        while True:
            # PLAYER1
            # If 1 player guesses the correct letter in the word, the turn will still belong to the next player to
            # ensure balance for the game.
            p1_move = spin_wheel()
            print("Player 1 spun for", p1_move)
            if p1_move == 'lose turn':  # skip player turn
                pass
            elif p1_move == 'spin again':  # player have to spin again and the procedure is the same with the main one
                p1_move = spin_wheel()
                print("Player 1 spun for", p1_move)
                if p1_move == 'lose turn':
                    pass
                elif p1_move == 'spin again':  # the game will break if the player receive 'spin again' more than once
                    print('congratulation! you break the game with your lucky')
                    all_values = player_dict.values()
                    max_value = max(all_values)
                    min_value = min(all_values)
                    if max_value == player_dict['p1']:  # find out who has the highest score
                        winner1 = player1
                        print('winner1 is player1')
                    elif max_value == player_dict['p2']:  # find out who has the highest score
                        winner1 = player2
                        print('winner1 is player2')
                    elif max_value == player_dict['p3']:  # find out who has the highest score
                        winner1 = player3
                        print('winner1 is player3')
                    if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                        winner2 = player1
                        print('winner2 is player1')
                    elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                        winner2 = player2
                        print('winner2 is player2')
                    elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                        winner2 = player3
                        print('winner2 is player2')
                    print(player_dict)
                    print('two players who have the highest score win the game')
                    break
                else:
                    p1_answer = input("Player 1, enter your answer here:  ").upper()  # answer of p1
                    print(player1 + ' ' + 'guessed' + ' ' + p1_answer)  # print the answer
                    new_string = phrase.count(p1_answer)  # count the number of letter in phrase
                    if p1_answer == 'bankruptcy'.upper():  # player can guess the whole word at any time they want
                        print('congratulation! you guess the whole phrase')
                        player_dict['p1'] = player_dict['p1'] + 1000
                        all_values = player_dict.values()
                        max_value = max(all_values)
                        min_value = min(all_values)
                        if max_value == player_dict['p1']:  # find out who has the highest score
                            winner1 = player1
                            print('winner1 is player1')
                        elif max_value == player_dict['p2']:  # find out who has the highest score
                            winner1 = player2
                            print('winner1 is player2')
                        elif max_value == player_dict['p3']:  # find out who has the highest score
                            winner1 = player3
                            print('winner1 is player3')
                        if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                            winner2 = player1
                            print('winner2 is player1')
                        elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                            winner2 = player2
                            print('winner2 is player2')
                        elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                            winner2 = player3
                            print('winner2 is player2')
                        print(player_dict)
                        print('two players who have the highest score win the game')
                        break
                    else:
                        if p1_answer in phrase and p1_answer not in guessed:
                            for i in range(2):  # loop to return the string
                                if p1_answer in phrase:
                                    index = phrase.index(p1_answer)
                                    guessed[index] = p1_answer  # the order of the guessed letter in the word
                                    phrase[index] = '_'  # replace it with underscores
                                else:
                                    print(''.join(guessed))
                                    if p1_answer != '':
                                        lstGuessed.append(p1_answer)  # fill in the guessed list
                                if '_' not in guessed:
                                    print('correct')
                            print('current guessed list is: ', lstGuessed)
                            if p1_move == 'double':
                                player_dict['p1'] = player_dict['p1'] * 2  # double the score
                                print('p1 points: ', player_dict['p1'])
                            elif p1_move == 'half':  # nothing will happen if they guess it right
                                player_dict['p1'] = player_dict['p1']
                                print('p1 points: ', player_dict['p1'])
                            elif p1_move == 'lose turn':
                                pass
                            else:
                                player_dict['p1'] += (p1_move * int(new_string))
                                print('p1 points: ', player_dict['p1'])
                            continue
                            if '_' in guessed:
                                continue
                            else:
                                break
                        else:  # if the player get it wrong
                            lstGuessed.append(p1_answer)  # fill the answer into the list with guessed letters
                            print('current guessed list is: ', lstGuessed)
                            if p1_move == 'half':  # divide by 2 if the answer is wrong
                                player_dict['p1'] = math.ceil(player_dict['p1'] / 2)
                                print('your answer is not correct or they are already guessed')
                                print('p1 points: ', player_dict['p1'])
                            else:
                                player_dict['p1'] = player_dict['p1']
                                print('p1 points: ', player_dict['p1'])
                                print('your answer is not correct or they are already guessed')
                            pass
                    if '_' not in guessed:
                        all_values = player_dict.values()
                        max_value = max(all_values)
                        min_value = min(all_values)
                        if max_value == player_dict['p1']:  # find out who has the highest score
                            winner1 = player1
                            print('winner1 is player1')
                        elif max_value == player_dict['p2']:  # find out who has the highest score
                            winner1 = player2
                            print('winner1 is player2')
                        elif max_value == player_dict['p3']:  # find out who has the highest score
                            winner1 = player3
                            print('winner1 is player3')
                        if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                            winner2 = player1
                            print('winner2 is player1')
                        elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                            winner2 = player2
                            print('winner2 is player2')
                        elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                            winner2 = player3
                            print('winner2 is player2')
                        print(player_dict)
                        print('two players who have the highest score win the game')
                        break

            else:
                p1_answer = input("Player 1, enter your answer here:  ").upper()  # answer of p1
                print(player1 + ' ' + 'guessed' + ' ' + p1_answer)  # print the answer
                new_string = phrase.count(p1_answer)  # count the number of letter in phrase
                if p1_answer == 'bankruptcy'.upper():  # if the player can guess the whole phrase
                    print('congratulation! you guess the whole phrase')
                    player_dict['p1'] = player_dict['p1'] + 1000  # return the value for the next game
                    all_values = player_dict.values()
                    max_value = max(all_values)
                    min_value = min(all_values)
                    if max_value == player_dict['p1']:  # find out who has the highest score
                        winner1 = player1
                        print('winner1 is player1')
                    elif max_value == player_dict['p2']:  # find out who has the highest score
                        winner1 = player2
                        print('winner1 is player2')
                    elif max_value == player_dict['p3']:  # find out who has the highest score
                        winner1 = player3
                        print('winner1 is player3')
                    if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                        winner2 = player1
                        print('winner2 is player1')
                    elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                        winner2 = player2
                        print('winner2 is player2')
                    elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                        winner2 = player3
                        print('winner2 is player2')
                    print(player_dict)
                    print('two players who have the highest score win the game')
                    break
                else:
                    if p1_answer in phrase and p1_answer not in guessed:  # if the player guess the wrong character
                        for i in range(2):  # loop to return the string
                            if p1_answer in phrase:  # index the character
                                index = phrase.index(p1_answer)
                                guessed[index] = p1_answer
                                phrase[index] = '_'
                            else:
                                print(''.join(guessed))
                                if p1_answer != '':
                                    lstGuessed.append(p1_answer)  # append to the guessed list
                            if '_' not in guessed:
                                print('correct')
                        print('current guessed list is: ', lstGuessed)
                        if p1_move == 'double':
                            player_dict['p1'] = player_dict['p1'] * 2  # double the score
                            print('p1 points: ', player_dict['p1'])
                        elif p1_move == 'half':  # nothing will happen if they guess it right
                            player_dict['p1'] = player_dict['p1']
                            print('p1 points: ', player_dict['p1'])
                        elif p1_move == 'lose turn':
                            pass
                        else:
                            player_dict['p1'] += (p1_move * int(new_string))
                            print('p1 points: ', player_dict['p1'])
                        if '_' in guessed:
                            continue
                        else:
                            all_values = player_dict.values()
                            max_value = max(all_values)
                            min_value = min(all_values)
                            if max_value == player_dict['p1']:  # find out who has the highest score
                                winner1 = player1
                                print('winner1 is player1')
                            elif max_value == player_dict['p2']:  # find out who has the highest score
                                winner1 = player2
                                print('winner1 is player2')
                            elif max_value == player_dict['p3']:  # find out who has the highest score
                                winner1 = player3
                                print('winner1 is player3')
                            if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                                winner2 = player1
                                print('winner2 is player1')
                            elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                                winner2 = player2
                                print('winner2 is player2')
                            elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                                winner2 = player3
                                print('winner2 is player2')
                            print(player_dict)
                            print('two players who have the highest score win the game')
                            break
                    else:
                        lstGuessed.append(p1_answer)
                        print('current guessed list is: ', lstGuessed)
                        if p1_move == 'half':  # divide by 2 if the answer is wrong
                            player_dict['p1'] = math.ceil(player_dict['p1'] / 2)
                            print('your answer is not correct or they are already guessed')
                            print('p1 points: ', player_dict['p1'])
                        else:
                            player_dict['p1'] = player_dict['p1']  # they guessed it wrong but nothing is taken as
                            # penalty
                            print('p1 points: ', player_dict['p1'])
                            print('your answer is not correct or they are already guessed')
                        break
    else:
        break

    # The code is basically the same as above, just change the name of each player
    # PLAYER2
    # If 1 player guesses the correct letter in the word, the turn will still belong to the next player to
    # ensure balance for the game.
    if '_' in guessed:
        while True:
            p2_move = spin_wheel()
            print("Player 2 spun for", p2_move)
            if p2_move == 'lose turn':
                break
            elif p2_move == 'spin again':
                p2_move = spin_wheel()
                print("Player 2 spun for", p2_move)
                if p2_move == 'lose turn':
                    break
                elif p2_move == 'spin again':
                    print('congratulation! you break the game with your lucky')
                    all_values = player_dict.values()
                    max_value = max(all_values)
                    min_value = min(all_values)
                    if max_value == player_dict['p1']:  # find out who has the highest score
                        winner1 = player1
                        print('winner1 is player1')
                    elif max_value == player_dict['p2']:  # find out who has the highest score
                        winner1 = player2
                        print('winner1 is player2')
                    elif max_value == player_dict['p3']:  # find out who has the highest score
                        winner1 = player3
                        print('winner1 is player3')
                    if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                        winner2 = player1
                        print('winner2 is player1')
                    elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                        winner2 = player2
                        print('winner2 is player2')
                    elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                        winner2 = player3
                        print('winner2 is player2')
                    print(player_dict)
                    print('two players who have the highest score win the game')
                    break
                else:
                    p2_answer = input("Player 2, enter your answer here:  ").upper()
                    print(player2 + ' ' + 'guessed' + ' ' + p2_answer)
                    new_string = phrase.count(p2_answer)
                    if p2_answer == 'bankruptcy'.upper():
                        print('congratulation! you guess the whole phrase')
                        player_dict['p2'] = player_dict['p2'] + 1000
                        all_values = player_dict.values()
                        max_value = max(all_values)
                        min_value = min(all_values)
                        if max_value == player_dict['p1']:  # find out who has the highest score
                            winner1 = player1
                            print('winner1 is player1')
                        elif max_value == player_dict['p2']:  # find out who has the highest score
                            winner1 = player2
                            print('winner1 is player2')
                        elif max_value == player_dict['p3']:  # find out who has the highest score
                            winner1 = player3
                            print('winner1 is player3')
                        if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                            winner2 = player1
                            print('winner2 is player1')
                        elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                            winner2 = player2
                            print('winner2 is player2')
                        elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                            winner2 = player3
                            print('winner2 is player2')
                        print(player_dict)
                        print('two players who have the highest score win the game')
                        break
                    else:
                        if p2_answer in phrase and p2_answer not in guessed:
                            for i in range(2):
                                if p2_answer in phrase:
                                    index = phrase.index(p2_answer)
                                    guessed[index] = p2_answer
                                    phrase[index] = '_'
                                else:
                                    print(''.join(guessed))
                                    if p2_answer != '':
                                        lstGuessed.append(p2_answer)
                                if '_' not in guessed:
                                    print('correct')
                            print('current guessed list is: ', lstGuessed)
                            if p2_move == 'double':
                                player_dict['p2'] = player_dict['p2'] * 2
                                print('p2 points: ', player_dict['p2'])
                            elif p2_move == 'half':
                                player_dict['p2'] = player_dict['p2']
                                print('p2 points: ', player_dict['p2'])
                            elif p2_move == 'lose turn':
                                break
                            else:
                                player_dict['p2'] += (p2_move * int(new_string))
                                print('p2 points: ', player_dict['p2'])
                            if '_' in guessed:
                                continue
                            else:
                                all_values = player_dict.values()
                                max_value = max(all_values)
                                min_value = min(all_values)
                                if max_value == player_dict['p1']:  # find out who has the highest score
                                    winner1 = player1
                                    print('winner1 is player1')
                                elif max_value == player_dict['p2']:  # find out who has the highest score
                                    winner1 = player2
                                    print('winner1 is player2')
                                elif max_value == player_dict['p3']:  # find out who has the highest score
                                    winner1 = player3
                                    print('winner1 is player3')
                                if max_value > player_dict['p1'] > min_value:  # find out who has the second highest
                                    # score
                                    winner2 = player1
                                    print('winner2 is player1')
                                elif max_value > player_dict['p2'] > min_value:  # find out who has the second
                                    # highest score
                                    winner2 = player2
                                    print('winner2 is player2')
                                elif max_value > player_dict['p3'] > min_value:  # find out who has the second
                                    # highest score
                                    winner2 = player3
                                    print('winner2 is player2')
                                print(player_dict)
                                print('two players who have the highest score win the game')
                                break

                        else:
                            lstGuessed.append(p2_answer)
                            print('current guessed list is: ', lstGuessed)
                            if p2_move == 'half':
                                player_dict['p2'] = math.ceil(player_dict['p2'] / 2)
                                print('p2 points: ', player_dict['p2'])
                            else:
                                player_dict['p2'] = player_dict['p2']
                                print('p2 points: ', player_dict['p2'])
                                print('your answer is not correct or they are already guessed')
                                break
                        if '_' not in guessed:
                            all_values = player_dict.values()
                            max_value = max(all_values)
                            min_value = min(all_values)
                            if max_value == player_dict['p1']:  # find out who has the highest score
                                winner1 = player1
                                print('winner1 is player1')
                            elif max_value == player_dict['p2']:  # find out who has the highest score
                                winner1 = player2
                                print('winner1 is player2')
                            elif max_value == player_dict['p3']:  # find out who has the highest score
                                winner1 = player3
                                print('winner1 is player3')
                            if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                                winner2 = player1
                                print('winner2 is player1')
                            elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                                winner2 = player2
                                print('winner2 is player2')
                            elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                                winner2 = player3
                                print('winner2 is player2')
                            print(player_dict)
                            print('two players who have the highest score win the game')
                            break

            else:
                p2_answer = input("Player 2, enter your answer here:  ").upper()
                print(player2 + ' ' + 'guessed' + ' ' + p2_answer)
                new_string = phrase.count(p2_answer)
                if p2_answer == 'bankruptcy'.upper():
                    print('congratulation! you guess the whole phrase')
                    player_dict['p2'] = player_dict['p2'] + 1000
                    all_values = player_dict.values()
                    max_value = max(all_values)
                    min_value = min(all_values)
                    if max_value == player_dict['p1']:  # find out who has the highest score
                        winner1 = player1
                        print('winner1 is player1')
                    elif max_value == player_dict['p2']:  # find out who has the highest score
                        winner1 = player2
                        print('winner1 is player2')
                    elif max_value == player_dict['p3']:  # find out who has the highest score
                        winner1 = player3
                        print('winner1 is player3')
                    if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                        winner2 = player1
                        print('winner2 is player1')
                    elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                        winner2 = player2
                        print('winner2 is player2')
                    elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                        winner2 = player3
                        print('winner2 is player2')
                    print(player_dict)
                    print('two players who have the highest score win the game')
                    break
                else:
                    if p2_answer in phrase and p2_answer not in guessed:
                        for i in range(2):
                            if p2_answer in phrase:
                                index = phrase.index(p2_answer)
                                guessed[index] = p2_answer
                                phrase[index] = '_'
                            else:
                                print(''.join(guessed))
                                if p2_answer != '':
                                    lstGuessed.append(p2_answer)
                            if '_' not in guessed:
                                print('correct')
                        print('current guessed list is: ', lstGuessed)
                        if p2_move == 'double':
                            player_dict['p2'] = player_dict['p2'] * 2
                            print('p2 points: ', player_dict['p2'])
                        elif p2_move == 'half':
                            player_dict['p2'] = player_dict['p2']
                            print('p2 points: ', player_dict['p2'])
                        elif p2_move == 'lose turn':
                            break
                        else:
                            player_dict['p2'] += (p2_move * int(new_string))
                            print('p2 points: ', player_dict['p2'])
                        if '_' in guessed:
                            continue
                        else:
                            all_values = player_dict.values()
                            max_value = max(all_values)
                            min_value = min(all_values)
                            if max_value == player_dict['p1']:  # find out who has the highest score
                                winner1 = player1
                                print('winner1 is player1')
                            elif max_value == player_dict['p2']:  # find out who has the highest score
                                winner1 = player2
                                print('winner1 is player2')
                            elif max_value == player_dict['p3']:  # find out who has the highest score
                                winner1 = player3
                                print('winner1 is player3')
                            if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                                winner2 = player1
                                print('winner2 is player1')
                            elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                                winner2 = player2
                                print('winner2 is player2')
                            elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                                winner2 = player3
                                print('winner2 is player2')
                            print(player_dict)
                            print('two players who have the highest score win the game')
                            break

                    else:
                        lstGuessed.append(p2_answer)
                        print('current guessed list is: ', lstGuessed)
                        if p2_move == 'half':
                            player_dict['p2'] = math.ceil(player_dict['p2'] / 2)
                            print('p2 points: ', player_dict['p2'])
                        else:
                            player_dict['p2'] = player_dict['p2']
                            print('p2 points: ', player_dict['p2'])
                            print('your answer is not correct or they are already guessed')
                            break
    else:
        break

    if '_' in guessed:
        while True:
            # PLAYER3
            # If 1 player guesses the correct letter in the word, the turn will still belong to the next player to
            # ensure balance for the game.
            p3_move = spin_wheel()
            print("Player 3 spun for", p3_move)
            if p3_move == 'lose turn':
                break
            elif p3_move == 'spin again':
                p3_move = spin_wheel()
                print("Player 3 spun for", p3_move)
                if p3_move == 'lose turn':
                    break
                elif p3_move == 'spin again':
                    print('congratulation! you break the game with your lucky')
                    all_values = player_dict.values()
                    max_value = max(all_values)
                    min_value = min(all_values)
                    if max_value == player_dict['p1']:  # find out who has the highest score
                        winner1 = player1
                        print('winner1 is player1')
                    elif max_value == player_dict['p2']:  # find out who has the highest score
                        winner1 = player2
                        print('winner1 is player2')
                    elif max_value == player_dict['p3']:  # find out who has the highest score
                        winner1 = player3
                        print('winner1 is player3')
                    if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                        winner2 = player1
                        print('winner2 is player1')
                    elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                        winner2 = player2
                        print('winner2 is player2')
                    elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                        winner2 = player3
                        print('winner2 is player2')
                    print(player_dict)
                    print('two players who have the highest score win the game')
                    break
                else:
                    p3_answer = input("Player 3, enter your answer here:  ").upper()
                    print(player3 + ' ' + 'guessed' + ' ' + p3_answer)
                    new_string = phrase.count(p3_answer)
                    if p3_answer == 'bankruptcy'.upper():
                        print('congratulation! you guess the whole phrase')
                        player_dict['p3'] = player_dict['p3'] + 1000
                        all_values = player_dict.values()
                        max_value = max(all_values)
                        min_value = min(all_values)
                        if max_value == player_dict['p1']:  # find out who has the highest score
                            winner1 = player1
                            print('winner1 is player1')
                        elif max_value == player_dict['p2']:  # find out who has the highest score
                            winner1 = player2
                            print('winner1 is player2')
                        elif max_value == player_dict['p3']:  # find out who has the highest score
                            winner1 = player3
                            print('winner1 is player3')
                        if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                            winner2 = player1
                            print('winner2 is player1')
                        elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                            winner2 = player2
                            print('winner2 is player2')
                        elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                            winner2 = player3
                            print('winner2 is player2')
                        print(player_dict)
                        print('two players who have the highest score win the game')
                        break
                    else:
                        if p3_answer in phrase and p3_answer not in guessed:
                            for i in range(2):
                                if p3_answer in phrase:
                                    index = phrase.index(p3_answer)
                                    guessed[index] = p3_answer
                                    phrase[index] = '_'
                                else:
                                    print(''.join(guessed))
                                    if p3_answer != '':
                                        lstGuessed.append(p3_answer)
                                if '_' not in guessed:
                                    print('correct')
                            print('current guessed list is: ', lstGuessed)
                            if p3_move == 'double':
                                player_dict['p3'] = player_dict['p3'] * 2
                                print('p3 points: ', player_dict['p3'])
                            elif p3_move == 'half':
                                player_dict['p3'] = player_dict['p3']
                                print('p3 points: ', player_dict['p3'])
                            elif p3_move == 'lose turn':
                                break
                            else:
                                player_dict['p3'] += (p3_move * int(new_string))
                                print('p3 points: ', player_dict['p3'])
                            if '_' in guessed:
                                continue
                            else:
                                all_values = player_dict.values()
                                max_value = max(all_values)
                                min_value = min(all_values)
                                if max_value == player_dict['p1']:  # find out who has the highest score
                                    winner1 = player1
                                    print('winner1 is player1')
                                elif max_value == player_dict['p2']:  # find out who has the highest score
                                    winner1 = player2
                                    print('winner1 is player2')
                                elif max_value == player_dict['p3']:  # find out who has the highest score
                                    winner1 = player3
                                    print('winner1 is player3')
                                if max_value > player_dict['p1'] > min_value:  # find out who has the second highest
                                    # score
                                    winner2 = player1
                                    print('winner2 is player1')
                                elif max_value > player_dict['p2'] > min_value:  # find out who has the second
                                    # highest score
                                    winner2 = player2
                                    print('winner2 is player2')
                                elif max_value > player_dict['p3'] > min_value:  # find out who has the second
                                    # highest score
                                    winner2 = player3
                                    print('winner2 is player2')
                                print(player_dict)
                                print('two players who have the highest score win the game')
                                break
                        if '_' not in guessed:
                            print(player_dict)
                            all_values = player_dict.values()
                            max_value = max(all_values)
                            min_value = min(all_values)
                            if max_value == player_dict['p1']:  # find out who has the highest score
                                winner1 = player1
                                print('winner1 is player1')
                            elif max_value == player_dict['p2']:  # find out who has the highest score
                                winner1 = player2
                                print('winner1 is player2')
                            elif max_value == player_dict['p3']:  # find out who has the highest score
                                winner1 = player3
                                print('winner1 is player3')
                            if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                                winner2 = player1
                                print('winner2 is player1')
                            elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                                winner2 = player2
                                print('winner2 is player2')
                            elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                                winner2 = player3
                                print('winner2 is player2')
                            print(player_dict)
                            print('two players who have the highest score win the game')
                            break

                        else:
                            lstGuessed.append(p3_answer)
                            print('current guessed list is: ', lstGuessed)
                            if p3_move == 'half':
                                player_dict['p3'] = math.ceil(player_dict['p3'] / 2)
                                print('p3 points: ', player_dict['p3'])
                            else:
                                player_dict['p3'] = player_dict['p3']
                                print('p3 points: ', player_dict['p3'])
                                print('your answer is not correct or they are already guessed')
                                break
                if '_' not in guessed:
                    print(player_dict)
                    all_values = player_dict.values()
                    max_value = max(all_values)
                    min_value = min(all_values)
                    if max_value == player_dict['p1']:  # find out who has the highest score
                        winner1 = player1
                        print('winner1 is player1')
                    elif max_value == player_dict['p2']:  # find out who has the highest score
                        winner1 = player2
                        print('winner1 is player2')
                    elif max_value == player_dict['p3']:  # find out who has the highest score
                        winner1 = player3
                        print('winner1 is player3')
                    if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                        winner2 = player1
                        print('winner2 is player1')
                    elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                        winner2 = player2
                        print('winner2 is player2')
                    elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                        winner2 = player3
                        print('winner2 is player2')
                    print(player_dict)
                    print('two players who have the highest score win the game')
                    break
            else:
                p3_answer = input("Player 3, enter your answer here:  ").upper()
                print(player3 + ' ' + 'guessed' + ' ' + p3_answer)
                new_string = phrase.count(p3_answer)
                if p3_answer == 'bankruptcy'.upper():
                    print('congratulation! you guess the whole phrase')
                    player_dict['p3'] = player_dict['p3'] + 1000
                    all_values = player_dict.values()
                    max_value = max(all_values)
                    min_value = min(all_values)
                    if max_value == player_dict['p1']:  # find out who has the highest score
                        winner1 = player1
                        print('winner1 is player1')
                    elif max_value == player_dict['p2']:  # find out who has the highest score
                        winner1 = player2
                        print('winner1 is player2')
                    elif max_value == player_dict['p3']:  # find out who has the highest score
                        winner1 = player3
                        print('winner1 is player3')
                    if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                        winner2 = player1
                        print('winner2 is player1')
                    elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                        winner2 = player2
                        print('winner2 is player2')
                    elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                        winner2 = player3
                        print('winner2 is player2')
                    print(player_dict)
                    print('two players who have the highest score win the game')
                    break
                else:
                    if p3_answer in phrase and p3_answer not in guessed:
                        for i in range(2):
                            if p3_answer in phrase:
                                index = phrase.index(p3_answer)
                                guessed[index] = p3_answer
                                phrase[index] = '_'
                            else:
                                print(''.join(guessed))
                                if p3_answer != '':
                                    lstGuessed.append(p3_answer)
                            if '_' not in guessed:
                                print('correct')
                        print('current guessed list is: ', lstGuessed)
                        if p3_move == 'double':
                            player_dict['p3'] = player_dict['p3'] * 2
                            print('p3 points: ', player_dict['p3'])
                        elif p3_move == 'half':
                            player_dict['p3'] = player_dict['p3']
                            print('p3 points: ', player_dict['p3'])
                        elif p3_move == 'lose turn':
                            break
                        else:
                            player_dict['p3'] += (p3_move * int(new_string))
                            print('p3 points: ', player_dict['p3'])
                        if '_' in guessed:
                            continue
                        else:
                            all_values = player_dict.values()
                            max_value = max(all_values)
                            min_value = min(all_values)
                            if max_value == player_dict['p1']:  # find out who has the highest score
                                winner1 = player1
                                print('winner1 is player1')
                            elif max_value == player_dict['p2']:  # find out who has the highest score
                                winner1 = player2
                                print('winner1 is player2')
                            elif max_value == player_dict['p3']:  # find out who has the highest score
                                winner1 = player3
                                print('winner1 is player3')
                            if max_value > player_dict['p1'] > min_value:  # find out who has the second highest score
                                winner2 = player1
                                print('winner2 is player1')
                            elif max_value > player_dict['p2'] > min_value:  # find out who has the second highest score
                                winner2 = player2
                                print('winner2 is player2')
                            elif max_value > player_dict['p3'] > min_value:  # find out who has the second highest score
                                winner2 = player3
                                print('winner2 is player2')
                            print(player_dict)
                            print('two players who have the highest score win the game')
                            break
                    else:
                        lstGuessed.append(p3_answer)
                        print('current guessed list is: ', lstGuessed)
                        if p3_move == 'half':
                            player_dict['p3'] = math.ceil(player_dict['p3'] / 2)
                            print('p3 points: ', player_dict['p3'])
                        else:
                            player_dict['p3'] = player_dict['p3']
                            print('p3 points: ', player_dict['p3'])
                            print('your answer is not correct or they are already guessed')
                        break
    else:
        break
# GAME2

# Introduction 2
print("""You two won the first game, now you'll move on to the next game to progress to the championship.
If the two of you tie, you will have to join together in mini game 1 to find the champion.
""")
time.sleep(1.5)

# Greetings and Rule of the game
print('''
|_   _| ___ \_   _| | | |_   _|/ _ \    |  __ \ / _ \ |  \/  ||  ___|
  | | | |_/ / | | | | | | | | / /_\ \   | |  \// /_\ \| .  . || |__  
  | | |    /  | | | | | | | | |  _  |   | | __ |  _  || |\/| ||  __| 
  | | | |\ \ _| |_\ \_/ /_| |_| | | |   | |_\ \| | | || |  | || |___ 
  \_/ \_| \_|\___/ \___/ \___/\_| |_/   \____/\_| |_/\_|  |_/\____/''')
time.sleep(1.5)
print("Please carefully read the rule.")
time.sleep(1.5)
print("""
- There are 15 steps in total. First the 2 players will roll the dice (in the program, not real life) to 
decide who will go first (the higher will go first). Then they take turn to roll it.
- In their turn, if he/she can answer the question related to Python programming correctly, they 
will advance the same number of steps as on the dice face value. If wrong, he/she move back 1 
step and lose the turn.
- The one that reaches the final step and answer correctly at the final step will be the winner. 
- If both the players have played for 5 rounds each and did not get to the final step, they both lose.
""")

isready = ""
while isready.lower() != "play":
    isready = input("Please type \"play\" to begin the game when you are ready: ")

print("Thank you for your time. Enjoy the game.")
time.sleep(1)


# This function asks player to roll the dice
def roll_the_dice():
    command = input(f"Player {winner1} please type 'roll' to roll the dice to decide who go first: ")
    while not command.lower() == "roll":  # this function asks again in case player type a wrong command
        print("Sorry we do not understand your command. Please type 'roll' again to continue.")
        command = input()
    if command.lower() == "roll":
        win1_dice = random.randrange(1, 7)  # Take random number from 1 to 6
    print(f'Your dice\'s value: {win1_dice}')
    # This function asks player to roll the dice
    command = input(f"Player {winner2} please type 'roll' to roll the dice to decide who go first: ")
    while not command.lower() == "roll":  # this function asks again in case player type a wrong command
        print("Sorry we do not understand your command. Please type 'roll' again to continue.")
        command = input()
    if command.lower() == "roll":
        win2_dice = random.randrange(1, 7)  # Take random number from 1 to 6
    print(f'Your dice\'s value: {win2_dice}')
    if win1_dice > win2_dice:
        print("Winner 1 go first.")
    elif win1_dice == win2_dice:
        roll_the_dice()
    else:
        print("Winner 2 go first.")
    return win1_dice, win2_dice


roll_the_dice()

step1 = 0  # step of player 1 is currently at
step2 = 0  # step of player 2 is currently at
turn1 = 0  # Turn of player 1 is currently in
turn2 = 0  # Turn of player 2 is currently in


class QA(object):  # initialise question, correct answer and other answer list
    def __init__(self, question, correctAnswer, otherAnswers):
        self.question = question
        self.correctAnsw = correctAnswer
        self.otherAnsw = otherAnswers


# Create a list of questions and answers
qaList = [QA("When was Python created?", "1990s", ["1980s", "2000s", "1970s"]),
          QA("Who invented Python?", "Guido van Rossum", ["James Gosling", "Larry Page", "Dennis Ritchie"]),
          QA("How many built-in functions does Python 3 have?", "68", ["52", "66", "64"]),
          QA("Which of these is not a core data type?", "Class", ["Tuples", "Dictionary", "Lists"]),
          QA('''What is the output of the following code :
L = ['a','b','c','d']
print("".join(L))''', "abcd", ["''", "Error", "dcba"]),
          QA("Which function overloads the >> operator?", "None of the above", ["more()", "gt()", "ge()"]),
          QA("time.time() returns...?",
             "	the current time in milliseconds since midnight, January 1, 1970 GMT (the Unix time)",
             ["the current time in milliseconds since midnight, January 1, 1970", "the current time",
              "the current time in milliseconds", "the current time in milliseconds since midnight"]),
          QA('''Which of the following statement(s) is TRUE?
A hash function takes a message of arbitrary length and generates a fixed length code.
A hash function takes a message of fixed length and generates a code of variable length.
A hash function may give the same hash value for distinct messages.''', "1 and 3 only",
             ["1 only", "2 and 3 only", "2 only", "None of them"]),
          QA('''Find the output of the following program:
A = dict() 
for x in enumerate(range(2)): 
    A[x[0]] = x[1] 
    A[x[1]+7] = x[0] 
    print(A) ''', "{0: 0, 7: 0, 1: 1, 8: 1}", ["{0: 1, 7: 0, 1: 1, 8: 0}", "{1: 1, 7: 2, 0: 1, 8: 1}", "Error"]),
          QA('''What is the output of the following?
i = 1
while True:
    if i % 5 == 0:
        break
    print(i)
    i + = 1''', "Syntax Error", ["1,2,3,4", "1,2,3,4,5", "1,3,5", "None of these"])]

count_round = 0
random.shuffle(qaList)  # This function randomly reorganise the order of the QAs in qaList

for item in qaList:
    time.sleep(2)
    # These functions from line 1801 to line 1810 evaluate the result of the game in case it is over
    if step1 >= 15 and step2 >= 15:
        print("This game is draw.")
        break
    elif step1 >= 15 and turn1 == turn2:
        print("Player 1 win this game.")
        break
    elif step2 >= 15:
        print("Player 2 win this game.")
        break
    # These functions from line 1812 to line 1819 confirm which player this turn belongs to
    if turn1 > turn2:
        print("Player 2's turn:")
        turn2 += 1
        is_turn1 = False
    else:
        print("Player 1's turn:")
        turn1 += 1
        is_turn1 = True
    print(item.question)  # Print out question
    print("Choose the correct one in the following possible answers:")
    choices = item.otherAnsw + [
        item.correctAnsw]  # Concatenate the correct answer with the other list by converting it to a list.
    random.shuffle(choices)  # This function randomly reorganise the order of possible choices in each question

    count_possAns = 0
    # Print out possible answers
    while count_possAns < len(choices):
        print(str(count_possAns + 1) + ": " + choices[count_possAns])
        count_possAns += 1

    print("Please enter the number of your answer:")
    playerAnsw = input()
    while not playerAnsw.isdigit():
        print("That was not a number. Please enter the number of your answer:")
        playerAnsw = input()
    playerAnsw = int(playerAnsw)

    # This function announce error in case the answer is not in the possible options
    while not (playerAnsw > 0 and playerAnsw <= len(choices)):
        print("That number doesn't correspond to any answer. Please enter the number of your answer:")
        playerAnsw = input()

    # Avoid too much information print on the screen at the same time
    time.sleep(0.5)
    print("Please wait for processing...")
    time.sleep(2)

    # For case player 1 chose a correct answer
    if choices[playerAnsw - 1] == item.correctAnsw and is_turn1 == True:
        print("Your answer was correct.")
        # This function asks player to roll the dice
        command = input("Player 1 please type 'roll' to roll the dice to move steps: ")
        while not command.lower() == "roll":  # this function asks again in case player type a wrong command
            print("Sorry we do not understand your command. Please type 'roll' again to continue.")
            command = input()
        if command.lower() == "roll":
            player1_dice = random.randrange(1, 7)  # Take random number from 1 to 6
        step1 += player1_dice

    # For case player 2 chose a correct answer
    elif choices[playerAnsw - 1] == item.correctAnsw and is_turn1 == False:
        print("Your answer was correct.")
        # This function asks player to roll the dice
        command = input("Player 2 please type 'roll' to roll the dice to move steps: ")
        while not command.lower() == "roll":  # this function asks again in case player type a wrong command
            print("Sorry we do not understand your command. Please type 'roll' again to continue.")
            command = input()
        if command.lower() == "roll":
            player2_dice = random.randrange(1, 7)  # Take random number from 1 to 6
        step2 += player2_dice

    # For case player 1 chose a wrong answer
    elif choices[playerAnsw - 1] != item.correctAnsw and is_turn1 == True:
        print(f'This is not a correct answer. Correct answer was: {item.correctAnsw}')
        print("You lose your turn.", end="\n")
        if step1 > 0:  # Backward 1 step only for player already step out of start point
            step1 -= 1

    # For case player 2 chose a wrong answer
    elif choices[playerAnsw - 1] != item.correctAnsw and is_turn1 == False:
        print(f'This is not a correct answer. Correct answer was: {item.correctAnsw}')
        print("You lose your turn.", end="\n")
        if step2 > 0:  # Backward 1 step only for player already step out of start point
            step2 -= 1

    # Conclude each round for both players
    if turn1 == turn2:
        count_round += 1
        print("Please wait for processing...")
        time.sleep(2)
        print(f'Round {count_round} is end. Player 1 has gone {step1} steps and player 2 has gone {step2} steps.')
if step1 < 15 and step2 < 15:  # For case both players did not get to the final step after 5 rounds
    print("Both player 1 and player 2 lost this game.")

# Mini game 1
print("""The rules of this game want us to compare the results of followers of 2 famous people in instagram.
If the player wins to get a point, otherwise loses all the points.
The winner of this game will be officially vaccinated. The loser will be injected after the 1st person.
In the meantime, the loser will be able to play mini game 2 while waiting for the winner.
""")
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'National Geographic',
        'follower_count': 135,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 133,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 131,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 127,
        'description': 'Reality TV personality and Model',
        'country': 'United States'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 119,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Nicki Minaj',
        'follower_count': 113,
        'description': 'Musician',
        'country': 'Trinidad and Tobago'
    },
    {
        'name': 'Nike',
        'follower_count': 109,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 108,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 107,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 94,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 90,
        'description': 'Reality TV personality',
        'country': 'United States'
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 89,
        'description': 'Comedian and actor',
        'country': 'United States'
    },
    {
        'name': 'Ellen DeGeneres',
        'follower_count': 87,
        'description': 'Comedian',
        'country': 'United States'
    },
    {
        'name': 'Real Madrid CF',
        'follower_count': 86,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'FC Barcelona',
        'follower_count': 85,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'Rihanna',
        'follower_count': 81,
        'description': 'Musician and businesswoman',
        'country': 'Barbados'
    },
    {
        'name': 'Demi Lovato',
        'follower_count': 80,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': "Victoria's Secret",
        'follower_count': 69,
        'description': 'Lingerie brand',
        'country': 'United States'
    },
    {
        'name': 'Zendaya',
        'follower_count': 68,
        'description': 'Actress and musician',
        'country': 'United States'
    },
    {
        'name': 'Shakira',
        'follower_count': 66,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Drake',
        'follower_count': 65,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Chris Brown',
        'follower_count': 64,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'LeBron James',
        'follower_count': 63,
        'description': 'Basketball player',
        'country': 'United States'
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 62,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Cardi B',
        'follower_count': 67,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'David Beckham',
        'follower_count': 82,
        'description': 'Footballer',
        'country': 'United Kingdom'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 61,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Justin Timberlake',
        'follower_count': 59,
        'description': 'Musician and actor',
        'country': 'United States'
    },
    {
        'name': 'UEFA Champions League',
        'follower_count': 58,
        'description': 'Club football competition',
        'country': 'Europe'
    },
    {
        'name': 'NASA',
        'follower_count': 56,
        'description': 'Space agency',
        'country': 'United States'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 100,
        'description': 'Actress',
        'country': 'United Kingdom'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 57,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 55,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Gigi Hadid',
        'follower_count': 54,
        'description': 'Model',
        'country': 'United States'
    },
    {
        'name': 'Priyanka Chopra Jonas',
        'follower_count': 53,
        'description': 'Actress and musician',
        'country': 'India'
    },
    {
        'name': '9GAG',
        'follower_count': 52,
        'description': 'Social media platform',
        'country': 'China'
    },
    {
        'name': 'Ronaldinho',
        'follower_count': 51,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'Maluma',
        'follower_count': 50,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Camila Cabello',
        'follower_count': 49,
        'description': 'Musician',
        'country': 'Cuba'
    },
    {
        'name': 'NBA',
        'follower_count': 47,
        'description': 'Club Basketball Competition',
        'country': 'United States'
    }
]
"""Information of players"""
player1 = input("Enter your name please: ")
print(f"Enter your name, and enjoy this game {player1}")
player2 = input("Put your name please: ")
print(f"Enter your name, and enjoy this game {player2}")

import random
import os


def get_random_account():
    """Get data from random account"""
    return random.choice(data)


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art
def game():
    print(logo)
    score_player1 = 0
    score_player2 = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        # Generate a random account from the game data.
        # Making account at position B become the next account at position A.
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        # Ask user for a guess
        print(f"Turn to player 1 {player1}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        """Get follower count of each account"""
        print(f"Player1 choose answer: {player1}")
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        # clear the screen between rounds.
        os.system("cls")
        print(logo)
        # Give user feedback on their guess.
        # Score keeping
        if is_correct:  # give user feedback on their guess.
            score_player1 += 1
            print(f"You're right! Current score of player 1: {score_player1}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score_player1}")

        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        # Ask user for a guess
        print(f"Turn to player 2 {player2}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        """Get follower count of each account"""
        print(f"Player2 choose answer: {player2}")
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        # clear the screen between rounds.
        os.system("cls")
        print(logo)
        # Give user feedback on their guess.
        # Score keeping
        if is_correct:  # give user feedback on their guess.
            score_player2 += 1
            print(f"You're right! Current score of player 2: {score_player2}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score_player2}")
        """The score determines the winner or loser."""
        if score_player1 > score_player2:
            print(f"Player 1 is winner {player1}")
        elif score_player1 < score_player2:
            print(f"Player 2 is winner {player2}")
        else:
            print("Deuce")


game()

# Mini game 2
import turtle  # Use turtle to create interface for player interaction
import time  # Call time to use sleep function to create time for player read the rules

print('''
______ _____ _   _ _____     _____   ___  ___  ___ _____ 
| ___ \  _  | \ | |  __ \   |  __ \ / _ \ |  \/  ||  ___|
| |_/ / | | |  \| | |  \/   | |  \// /_\ \| .  . || |__  
|  __/| | | | . ` | | __    | | __ |  _  || |\/| ||  __| 
| |   \ \_/ / |\  | |_\ \   | |_\ \| | | || |  | || |___ 
\_|    \___/\_| \_/\____/    \____/\_| |_/\_|  |_/\____/ ''')
time.sleep(1.5)
print("""You will be participating in this game in the meantime, so try to survive as long as possible.
In this game, you will have to catch the balls continuously and not let them pass. 
There are a total of 4 balls, if you miss 2 ball, you will lose immediately. 
Because there are many technical limitations, please try to catch the ball in the center of the paddle, 
if you catch it at the edge, the ball will go through (Use button 'z' and 'c' to move the paddle). """)

time.sleep(25)
# This code is used to create screen
sg2 = turtle.Screen()
sg2.title("Sub game 2")
sg2.bgcolor("black")
sg2.setup(width=600, height=800)

# Players' scores
Player = 0

# Show points
s_point = turtle.Turtle()
s_point.speed(0)
s_point.color("white")
s_point.penup()
s_point.hideturtle()
s_point.goto(0, -375)
s_point.write("Player : 0", align="center", font=("Arial", 28, "bold"))

# This code is used to create the paddle 2
pad = turtle.Turtle()
pad.speed(0)
pad.shape("square")
pad.color("white")
pad.shapesize(stretch_wid=1, stretch_len=6)
pad.penup()
pad.goto(0, -300)

# This code is used to create the ball
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("circle")
ball1.color("red")
ball1.penup()
ball1.goto(150, 150)
ball1.dx = -9
ball1.dy = -9

ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("circle")
ball2.color("blue")
ball2.penup()
ball2.goto(-150, 180)
ball2.dx = 9
ball2.dy = 9

ball3 = turtle.Turtle()
ball3.speed(0)
ball3.shape("circle")
ball3.color("purple")
ball3.penup()
ball3.goto(-230, -200)
ball3.dx = 9
ball3.dy = 9

ball4 = turtle.Turtle()
ball4.speed(0)
ball4.shape("circle")
ball4.color("orange")
ball4.penup()
ball4.goto(230, -100)
ball4.dx = 9
ball4.dy = 9


# This code is used to create the function
def pad_move_left():  # Paddle 1 move left
    x = pad.xcor()
    x = x + 50
    pad.setx(x)


def pad_move_right():  # Paddle 1 move right
    x = pad.xcor()
    x = x - 50
    pad.setx(x)


# This code is used to create a move button for 2 playersz
sg2.listen()
sg2.onkeypress(pad_move_right, "z")
sg2.onkeypress(pad_move_left, "c")

# This code is used to create the loop for the game
while True:
    # This code is used to make the turtle window keep updating
    sg2.update()

    # This code is used to make the paddle flexible by creating a coordinate connection between left and right
    if pad.xcor() > 290:
        pad.goto(-290, -300)

    if pad.xcor() < -290:
        pad.goto(290, -300)

    # These two command line is used to make the ball move
    ball1.setx(ball1.xcor() + ball1.dx)
    ball1.sety(ball1.ycor() + ball1.dy)

    # This code is used to create the direction for the ball 1.
    # With the following 2 lines, the ball will bounce back when it hits the edge of the screen.
    if ball1.xcor() > 290:
        ball1.setx(290)
        ball1.dx *= -1

    if ball1.xcor() < -290:
        ball1.setx(-290)
        ball1.dx *= -1

    if ball1.ycor() > 390:
        ball1.sety(390)
        ball1.dy *= -1

    # This code is used to calculate the score and remove the ball from the game screen.
    if ball1.ycor() < -400:
        ball1.sety(-400)
        ball1.reset()
        ball1.dx *= -1
        Player -= 1
        s_point.clear()
        s_point.write("Player : {}".format(Player), align="center", font=("Arial", 28, "bold"))

    # This code is used to create interaction between ball and paddle
    if (-280 < ball1.ycor() < -270) and (pad.xcor() - 50 < ball1.xcor() < pad.xcor() + 50):
        ball1.sety(-270)
        ball1.dy *= -1

    # These two command line is used to make the ball move
    ball2.setx(ball2.xcor() + ball2.dx)
    ball2.sety(ball2.ycor() + ball2.dy)

    # This code is used to create the direction for the ball 1, with the following 2 lines, the ball will bounce back when it hits the edge of the screen.
    if ball2.xcor() > 290:
        ball2.setx(290)
        ball2.dx *= -1

    if ball2.xcor() < -290:
        ball2.setx(-290)
        ball2.dx *= -1

    if ball2.ycor() > 390:
        ball2.sety(390)
        ball2.dy *= -1

    # This code is used to calculate the score and remove the ball from the game screen.
    if ball2.ycor() < -400:
        ball2.sety(-400)
        ball2.reset()
        ball2.dx *= -1
        Player -= 1
        s_point.clear()
        s_point.write("Player : {}".format(Player), align="center", font=("Arial", 28, "bold"))

    # This code is used to create interaction between ball and paddle
    if (-280 < ball2.ycor() < -270) and (pad.xcor() - 50 < ball2.xcor() < pad.xcor() + 50):
        ball2.sety(-270)
        ball2.dy *= -1

    # These two command line is used to make the ball move
    ball3.setx(ball3.xcor() + ball3.dx)
    ball3.sety(ball3.ycor() + ball3.dy)

    # This code is used to create the direction for the ball 1, with the following 2 lines, the ball will bounce back when it hits the edge of the screen.
    if ball3.xcor() > 290:
        ball3.setx(290)
        ball3.dx *= -1

    if ball3.xcor() < -290:
        ball3.setx(-290)
        ball3.dx *= -1

    if ball3.ycor() > 390:
        ball3.sety(390)
        ball3.dy *= -1

    # This code is used to calculate the score and remove the ball from the game screen.
    if ball3.ycor() < -400:
        ball3.sety(-400)
        ball3.reset()
        ball3.dx *= -1
        Player -= 1
        s_point.clear()
        s_point.write("Player : {}".format(Player), align="center", font=("Arial", 28, "bold"))

    # This code is used to create interaction between ball and paddle
    if (-280 < ball3.ycor() < -270) and (pad.xcor() - 50 < ball3.xcor() < pad.xcor() + 50):
        ball3.sety(-270)
        ball3.dy *= -1

    # These two command line is used to make the ball move
    ball4.setx(ball4.xcor() + ball4.dx)
    ball4.sety(ball4.ycor() + ball4.dy)

    # This code is used to create the direction for the ball 1, with the following 2 lines, the ball will bounce back when it hits the edge of the screen.
    if ball4.xcor() > 290:
        ball4.setx(290)
        ball4.dx *= -1

    if ball4.xcor() < -290:
        ball4.setx(-290)
        ball4.dx *= -1

    if ball4.ycor() > 390:
        ball4.sety(390)
        ball4.dy *= -1

    # This code is used to calculate the score and remove the ball from the game screen.
    if ball4.ycor() < -400:
        ball4.sety(-400)
        ball4.reset()
        ball4.dx *= -1
        Player -= 1
        s_point.clear()
        s_point.write("Player : {}".format(Player), align="center", font=("Arial", 28, "bold"))

    # This code is used to create interaction between ball and paddle
    if (-280 < ball4.ycor() < -270) and (pad.xcor() - 50 < ball4.xcor() < pad.xcor() + 50):
        ball4.sety(-270)
        ball4.dy *= -1

    # This code is used to end the game
    if Player == -1:
        sg2.clearscreen()
    sg2.exitonclick()
