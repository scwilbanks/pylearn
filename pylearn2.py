#!/usr/bin/env python3

from sys import argv
from random import shuffle
import json
from datetime import *
import os.path

"""
-edit cards
-make menu function
-play sound with 
-shuffle cards before starting
-make functions for pre answer menu and post answer menu
--post answer menu gives option to edit card
--edit card by prompting input with current as prompt, return to update
-make outro of each card to clean up main function
-/d for data on card
-statistics
-when card is deleted, continues to count it in cards remaining
"""

PATH = 'decks/'+argv[1]+'.json'

def load_from_old(deck):
    from decks.python3 import Questions
    qdeck = Questions()
    newdata = {}
    with open(PATH, 'r') as file:
        data = file.read()
        data = json.loads(data)
        for card in data:
            newdata[card] = {
                'Prompt': qdeck[card], 
                'Sound': 0,
                'Ease': 1.3,
                'Interval': 1.0,
                'Due': 0,
                'First Seen': date.toordinal(date.today()),
                'Last Review': 0,
                'Reviews': 0,
                'Lapses': 0,
                'Total time': 0,
                'Average Time': 0,
                'Deck': deck
                }
        
    with open(PATH, 'w') as file:
        file.write(json.dumps(newdata))


def make_todayscards():
    with open(PATH, 'r') as file:
        data = file.read()
    todayscards = []
    if not data:
        return todayscards
    deck = json.loads(data)
    for card in deck:
        if round(deck[card]['Due']) < date.toordinal(date.today()):
            todayscards.append([deck[card]['Due'], card])
    shuffle(todayscards)
    #todayscards.sort
    return todayscards


def evaluate(answer, card):
    
    with open(PATH, 'r') as file:
        data = file.read()
    deck = json.loads(data)

    if answer == '2':
        correct = True
        deck[card]['Ease'] = max(1.3, deck[card]['Ease']*.85)
        deck[card]['Interval'] *= 1.2
    elif answer == '3':
        correct = True
        deck[card]['Interval'] *= deck[card]['Ease']
    elif answer == '4' or answer == card:
        correct = True
        deck[card]['Ease'] *= 1.25
        deck[card]['Interval'] *= deck[card]['Ease']
    else:
        correct = False
        deck[card]['Ease'] = max(1.3, deck[card]['Ease']*.8)
        deck[card]['Interval'] *= deck[card]['Ease']
        deck[card]['Lapses'] += 1

    deck[card]['Due'] = date.toordinal(date.today())+deck[card]['Interval']
    deck[card]['Last Review'] = date.toordinal(date.today())
    deck[card]['Reviews'] += 1

    print()
    if correct:
        print('Correct!\n\n'+card+'\n')
    else:
        print('Incorrect. Correct answer:\n\n'+card+'\n')
    print('Due again in', round(deck[card]['Interval']), 'days.')
        #Decide if I want to round this how it is, up, or down.
        #make sure rounding makes since and make this accurate

    with open(PATH, 'w') as file:
        file.write(json.dumps(deck))

    return correct

def edit_card(card):
    pass


def delete_card(card):
    with open(PATH, 'r') as file:
        data = file.read()
    if data:
        deck = json.loads(data)
    else:
        deck = {}
    print(type(card))
    del deck[card]
    with open(PATH, 'w') as file:
        file.write(json.dumps(deck))


def add_card():
    with open(PATH, 'r') as file:
        data = file.read()
    if data:
        deck = json.loads(data)
    else:
        deck = {}

    card = input('Answer for card:\n\n')
    assert card not in deck
    prompt = input('Prompt for card:\n\n')
    sound = input('Sound to play on prompt: Filename.mp3 or leave blank:\n\n')

    deck[card] = {
        'Prompt': prompt, 
        'Sound': sound,
        'Ease': 1.3,
        'Interval': 1.0,
        'Due': 0,
        'First Seen': date.toordinal(date.today()),
        'Last Review': 0,
        'Reviews': 0,
        'Lapses': 0,
        'Total time': 0,
        'Average Time': 0,
        'Deck': argv[1]
        }

    with open(PATH, 'w') as file:
        file.write(json.dumps(deck))


def menu():
    pass


def main():
    if os.path.exists(PATH):
        with open(PATH, 'r') as file:
            data = file.read()
            if data:
                deck = json.loads(data)
    else:
        with open(PATH, 'w') as file:
            pass
        deck = {}
    todayscards = make_todayscards()
    print('--------------------------\n')
    print('Studying '+str(len(todayscards))+' cards today.\n')
    print("/a:   Add card\n/del: Delete card\n/q:   Quit studying\n")
    #I should consolidate all this menu stuff to one function
    menuprompt = input()
    if menuprompt == '/a':
        add_card()
    count = 0
    for card in todayscards:
        print('--------------------------')
        print(deck[card[1]]['Prompt'])
        print()
        menu = True
        while menu:
            answer = input('>>> ')
            if answer == '/q':
                quit()
            elif answer == '/e':
                #edit(card)
                pass
            elif answer == '/a':
                add_card()
            elif answer == '/del':
                delete_card(card[1])
                print("Card deleted")
                menu = False
                print('\n'+str(len(todayscards)-count)+' cards left.')
            else:
                menu = False
                if not evaluate(answer, card[1]):
                    #relearning 1min, 10mins, then make due tomorrow
                    #dont change ease, already degraded when wrong answer
                    #make new arr for relearns. add with bisect.insort_left
                    #probably just search when it inserts a new one
                    #for each card check if next relearn is due, then dequeue
                    pass
                count += 1
                print('\n'+str(len(todayscards)-count)+' cards left.')
                input()#/d to display card data
                
                
main()
