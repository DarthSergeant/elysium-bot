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

def questions(sentence, name):
    ###Question Prep###
    seperate_questionmark = sentence.replace('?', ' ?')
    sentence_list = seperate_questionmark.split(" ") #makes each word a list item
    if any(word in sentence_list for word in replacement):
        if 'a' in sentence_list:
            sentence_list.remove('a')
        if 'an' in sentence_list:
            sentence_list.remove('an')
        if 'the' in sentence_list:
            sentence_list.remove('the')
        if 'you' in sentence_list:
            sentence_list = [w.replace('you', 'me') for w in sentence_list]
    if " or " in sentence:
        divider_word = sentence_list.index('or')
        choices = [sentence_list[divider_word-1], sentence_list[divider_word+1]]
        selection = random.randint(0,1)
        msg = choices[selection]
        return msg
    elif any(word in sentence for word in five_ws):
        msg = "Your w words confused me."
        return msg
    else:
        num = random.randint(0, (len(eight_ball)-1))
        msg = eight_ball[num]
        return msg
    
def create_response(sentence, name):
    msg = {}
    if sentence == "test":
        msg = "All systems are go"
        time.sleep(1)
        return msg
    if any(word in sentence for word in bot_tags):
        if "?" in sentence:
            msg = questions(sentence, name)
            time.sleep(1)
            return msg