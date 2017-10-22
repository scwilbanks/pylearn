from random import shuffle
from sys import argv
from datetime import date
import json
from time import sleep
from os.path import isfile

"""
Takes randomized list of questions and checks input against answer.

Also saves scores for spaced repetition.
"""

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
    sleep(1)
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
    result = input(">>> ")
    if result == '/q':
        quit()
    return result==ans

def Start(questions):
    keys = list(questions.keys())
    shuffle(keys)
    finished = "You are finisheding with studying ",subject+"!"
    today = [finished]
    for key in keys:
        if scores[key][1] <= date.toordinal(date.today()):
            today.insert(-1, key)
    print()
    print('You will study', len(today)-1, "items today.")
    sleep(1)
    for key in today:
        print()
        if len(today) == 1:
            print(''.join(finished))
            today.clear()
            break
        print()
        print("____________________________")
        print()
        res = MakeQuestion(key, questions[key])
        ChangeScore(key, res)
        if res == True:
            today.remove(key)
        elif res == False:
            today.insert(-1, key)
        print(len(today)-1, "items left today.")
    return

subject = argv[1]
exec("from decks."+subject+" import Questions")

questions = Questions()
scores = GetScores(questions)

Start(questions)
