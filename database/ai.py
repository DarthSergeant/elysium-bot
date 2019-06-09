import random
import time

#8 Ball
eight_ball = ['It is certain', ' It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
              'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
              'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
              'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no',
              'Outlook not so good', 'Very doubtful', 'Concentrate and ask again... just kidding.  NO.']

five_ws = ['who', 'what', 'when', 'where', 'why', 'how']
bot_tags = ['@elysia', '@ely', 'ely', 'elysia', ',,']
replacement = ['you', 'a', 'an', 'the']
#dnd_stats = ['str', 'int', 'wis', 'cha', 'con']

def process_sentence(sentence, name): #Used to create the refined variable used for processing
    seperate_comma = sentence.replace(',,', ' ,,') #,, is most common tag so this seperates it if a space is not used
    seperate_questionmark = seperate_comma.replace('?', ' ?') #? is another common identifier so this makes sure it doesn't get combined with the data
    sentence_list = seperate_questionmark.split(" ") #Makes sentence into a list
    remove_words = True
    while remove_words:
        if any(word in sentence_list for word in replacement):
                if 'a' in sentence_list:
                    sentence_list.remove('a')
                if 'an' in sentence_list:
                    sentence_list.remove('an')
                if 'the' in sentence_list:
                    sentence_list.remove('the')
                if 'you' in sentence_list:
                    sentence_list = [w.replace('you', 'me') for w in sentence_list]
        else:
            remove_words = False
        return sentence_list
    
def questions(refined):
    if "or" in refined:
        divider_word = refined.index('or')
        choices = [refined[divider_word-1], refined[divider_word+1]]
        selection = random.randint(0,1)
        msg = choices[selection]
        return msg
    elif any(word in refined for word in five_ws):
        msg = "Your w words confused me."
        return msg
    else:
        num = random.randint(0, (len(eight_ball)-1))
        msg = eight_ball[num]
        return msg

def dice_roller(refined):
    divider_word = refined.index('roll')
    number = refined[divider_word+1]
    if number.isdigit() == True:
        msg = random.randint(0, int(number))
        return msg
    else:
        msg = "I only work with numerals"
        return msg

def create_response(sentence, name):
    msg = {}
    if sentence == "test":
        msg = "All systems are go"
    if sentence == 'wooloo': #Temporarily removes need to use tags.  Bot will respond to everything relevant
        bot_tags.append(' ')
        msg = "Tags removed."
    if any(word in sentence for word in bot_tags):
        refined = process_sentence(sentence, name)
        if "?" in sentence:
            msg = questions(refined)
        if "roll" in sentence:
            msg = dice_roller(refined)
    time.sleep(.75)
    return msg
            
