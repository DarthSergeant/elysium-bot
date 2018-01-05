import random
from database.cat_facts import catfacts
from database.reactions import reaction
from database.images import cruise, lasagna
#Make this one database

bulli = ['nerd', 'shut up', 'kys', 'nurd', 'loser', 'git gud', 'noob', 'newb', 'n00b', 'stupid', 'idiot', 'dumb', 'dum',
        'shut it', 'up shut', 'idot', 'ideot', 'baka', 'retard']
   
#8 Ball
eight_ball = ['It is certain', ' It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
              'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
              'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
              'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no',
              'Outlook not so good', 'Very doubtful']

NUMBER = 0
def create_response(sentence, name, parse):
    global NUMBER
    msg = {}
    

    #Name Based
    if "IFTTT" in name:
        echo = parse
        msg = echo
    #Limited Responses
    if "no" in sentence:
        NUMBER+=1
        if NUMBER%3 == 0:
                msg = "no u"
    if "911" in sentence:
        NUMBER+=1
        if NUMBER%2 == 0:
                msg = '911'
    if "awoo" in sentence:
        NUMBER+=1
        if NUMBER%2 == 0:
                msg = "Awooo"
    if 'fite' in sentence:
        NUMBER+=1
        if NUMBER%2 == 0:
                msg = "fite me"
    if 'tulta' in sentence:
        NUMBER+=1
        if NUMBER%2 == 0:
                msg = 'tulta'
        
    #Responses
    if 'satan' in sentence:
        msg = 'Thats me.'
    if any(word in sentence for word in bulli):
        msg = "pls no bulli"
    if 'league' in sentence:
        msg = 'No, David.'
    if len(sentence) > 220:
        msg = "lol do you really expect me to read that?"
    
    #Disable Response
    if '..' in sentence:
        msg = {}    

    #Commands
    if  '!8ball' in sentence:
        num = random.randint(0, (len(eight_ball)-1))
        msg = eight_ball[num]
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
    if sentence == '!cruise':
        num = random.randint(0,(len(cruise)-1))
        msg = cruise[num]
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
    if sentence == '!weeb':
        msg = reaction[7]
    if sentence == '!wth':
        msg = reaction[8]
    if sentence == '!shark':
        msg = reaction[9]

    return msg
