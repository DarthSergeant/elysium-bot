import random
from database.cat_facts import catfacts
from database.lasagna import lasagna
from database.reactions import reaction
#Make this one database

def create_response(sentence):
    msg = {}
    
    #Responses
    if "no" in sentence:
        msg = "no u"
    if "911" in sentence:
        msg = '911'
    if "awoo" in sentence:
        msg = "awooo"
    if 'fite' in sentence:
        msg = "fite me"
    if 'tulta' in sentence:
        msg = 'tulta'
    if 'league' in sentence:
        msg = 'No, David.'

    #Commands
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

    return msg
