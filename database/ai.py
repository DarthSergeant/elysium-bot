import random
from database.cat_facts import catfacts
from database.lasagna import lasagna
from database.reactions import reaction
#Make this one database

bulli = ['nerd', 'shut up', 'kys', 'nurd', 'loser', 'git gud', 'noob', 'newb', 'n00b', 'stupid', 'idiot', 'dumb', 'dum',
        'shut it', 'up shut', 'idot', 'ideot', 'baka', 'retard']

NUMBER = 0
def create_response(sentence):
    global NUMBER
    msg = {}
    
    #Responses
    if any(word in sentence for word in bulli):
        msg = "pls no bulli"
    if "no" in sentence:
        msg = "no u"
    if "not david" in sentence:
        msg = "I don't care."
    if "911" in sentence:
        msg = '911'
    if "awoo" in sentence:
        msg = "Awooo"
    if 'fite' in sentence:
        msg = "fite me"
    if 'tulta' in sentence:
        msg = 'tulta'
    if 'league' in sentence:
        msg = 'No, David.'
    if 'satan' in sentence:
        msg = 'Thats me.'
    if 'lit' in sentence:
        msg = 'Its lit fam'
    if '420' in sentence:
        msg = 'Blaze it.'
    if '4:20' in sentence:
        msg = 'Blaze it.'
    if '..' in sentence:
        msg = {}    
    if len(sentence) > 170:
        msg = "lol do you really expect me to read that?"


    #Commands
    if sentence == '!count':
        NUMBER +=1
        msg = NUMBER
    if sentence == '!roll20':
        num = ((random.randint(0,19))+1)
        msg = num
    if sentence == '!roll6':
        num = ((random.randint(0,5))+1)
        msg = num
    if sentence == '!lasagna':
        num = random.randint(0,(len(lasagna)-1))
        msg = lasagna[num]
    if sentence == '!catfacts':
        num = random.randint(0, (len(catfacts)-1))
        msg = catfacts[num]
    if sentence == '!thanks':
        msg = reaction[0]
    if sentence == '!dog':
        msg = reaction[1]
    if sentence == '!confuse':
        msg = reaction[2]
    if sentence == '!stop':
        msg = reaction[3]
    if sentence == '!obama':
        msg = reaction[4]
    if sentence == '!re':
        msg = reaction[5]
    if sentence == '!whatever':
        msg = reaction[6]

    return msg
