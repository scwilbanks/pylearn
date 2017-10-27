from random import shuffle
from sys import argv
from datetime import date
import json
from time import sleep
from os.path import isfile
import pygame
from pygame import mixer

"""
Takes randomized list of questions and checks input against answer. Plays accompanying sound file if there is one in the sound folder.

Also saves scores for spaced repetition.
"""

def PlaySound(filename):
    f = 'sounds/'+subject+'/'+filename+'.mp3'
    if isfile(f):
        pygame.mixer.music.load(f)
        pygame.mixer.music.play()

def GetQuestions(subject):
    pass

def ChangeScore(key, ans):
    score = scores[key][0]
    if ans == True:
        pre = 'Correct!'
        if score <= 1:
            score += 1
        elif score > 1:
            score *= 2
        else:
            return "ERROR Change Score"
    elif ans == False:
        pre = "Incorrect. Correct answer:\n\n"+key+"\n"
        score = 0
    else:
        return "ERROR Change Score"
    print()
    scores[key] = [score, date.toordinal(date.today())+score]
    if score == 0:
        print(pre)
        sleep(1)
        print('Due again today.')
    elif score == 1:
        print(pre+' Due again tomorrow.')
    elif score > 1:
        print(pre+' Due again in '+str(score)+' days.')
    else:
        return 'ERROR Change Score'
    sleep(.5)
    print()
    with open('scores/'+subject+'.json', 'w') as file:
        file.write(json.dumps(scores))

def GetScores(questions):
    if isfile('scores/'+subject+'.json'):
        with open('scores/'+subject+'.json', 'r') as file:
            data = file.read()
            oldscores = json.loads(data)
    elif not isfile('scores/'+subject+'.json'):
        oldscores = {}
    scores = {}
    for prompt in questions:
        if prompt in oldscores:
            scores[prompt] = oldscores[prompt]
        elif prompt not in oldscores:
            scores[prompt] = [0, date.toordinal(date.today())]
        else:
            return "ERROR GetScores"
    with open('scores/'+subject+'.json', 'w') as file:
        file.write(json.dumps(scores))
    return scores

def MakeQuestion(ans, prompt):
    print(prompt)
    while True:
        PlaySound(prompt)
        result = input(">>> ")
        print(result)
        if result == '':
            print(ans)
            pass
        elif result == '/q':
            quit()
        elif result == '/s':
            pass
        elif result == '1':
            return False
        elif result == '2':
            return True
        else:
            return result==ans

def Start(questions):
    pygame.init()
    pygame.mixer.init()
    keys = list(questions.keys())
    if mode == 'shuffle':
        shuffle(keys)
    elif mode == 'shortestpromptfirst':
        keys.clear()
        vals = questions.values()
        vals = sorted(list(vals), key=len)
        for val in vals:
            keys.append(list(questions.keys())[list(questions.values()).index(val)])
    finished = "You are finisheding with studying ",subject+"!"
    today = []
    for key in keys:
        if scores[key][1] <= date.toordinal(date.today()):
            today.insert(-1, key)
    print()
    print('You will study', len(today), 'of', len(keys), "items today.")
    sleep(.5)
    while len(today) > 0:
        for key in today:
            print()
            print("____________________________")
            print()
            res = MakeQuestion(key, questions[key])
            ChangeScore(key, res)
            if res == True:
                today.remove(key)
            elif res == False:
                today.insert(-1, key)
            print(len(today), "items left today.")
    print(''.join(finished))
    return

subject = argv[1]
exec("from decks."+subject+" import Questions")

if len(argv) > 2:
    mode = argv[2]
else:
    mode = 'shuffle'

questions = Questions()
scores = GetScores(questions)

Start(questions)
