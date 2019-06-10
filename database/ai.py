import random
import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

#8 Ball
eight_ball = ['It is certain', ' It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
              'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
              'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
              'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no',
              'Outlook not so good', 'Very doubtful', 'Concentrate and ask again... just kidding.  NO.']

five_ws = ['who', 'what', 'when', 'where', 'why', 'how']
bot_tags = ['@elysia', '@ely', 'ely', 'elysia', ',,']
replacement = ['you', 'a', 'an', 'the']
dnd_stats = ['str', 'int', 'wis', 'cha', 'con']

def process_sentence(sentence, name): #Used to create the refined variable used for processing
    seperate_comma = sentence.replace(',,', '') #,, is most common tag so this seperates it if a space is not used
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

def clean_price(price):
    price_string = str(price)
    price_split_1 = price_string.split(">")[1]
    price_split_2 = price_split_1.split("<")[0]
    price_split = price_split_2.strip()
    return price_split

def ge_search(refined):
    refined.remove('price')
    if '' in refined:
        refined.remove('')
    item = ' '.join(refined) #converts list back to a string
    formatted_item = item.replace(' ', '-')
    url_status = True
    url = "https://www.ge-tracker.com/item/" + formatted_item
    req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
    try:
        webpage = urlopen(req).read()
    except:
        msg ='Cant find item'
        url_status = False       
    if url_status:
        soup = BeautifulSoup(webpage, "html.parser")
        sell_price = soup.find("td", {'id': 'item_stat_sell_price'})
        offer_price = soup.find("td", {'id': 'item_stat_offer_price'})
        msg = (item+
                ('\nSell Price: ')+clean_price(sell_price)+ 
               ('\nOffer Price: ')+clean_price(offer_price))
    return msg

def questions(refined):
    if "or" in refined:
        divider_word = refined.index('or')
        choices = [refined[divider_word-1], refined[divider_word+1]]
        selection = random.randint(0,1)
        msg = choices[selection]
    elif any(word in refined for word in five_ws):
        msg = "Your w words confused me."
    else:
        num = random.randint(0, (len(eight_ball)-1))
        msg = eight_ball[num]
    return msg

def dice_roller(refined):
    divider_word = refined.index('roll')
    number = refined[divider_word+1]
    if number.isdigit() == True:
        if int(number) > 1000000001:
            msg = "Too high"
        else:
            msg = (random.randint(0, int(number))+1)
    else:
        msg = "I only work with positive integers"
    return msg

def dnd_stat_calc(refined):
    raw_stat_name = (set(refined).intersection(dnd_stats))
    stat_list = list(raw_stat_name) #Converts set to list 
    stat_name = stat_list[0] #Picks only the first stat name just incase multiples were typed in the message
    roll = [(random.randint(0,5)+1) for n in range(4)]
    roll.sort()
    del roll[0]
    stat_value = str(sum(roll))
    msg = ((stat_name)+':'+(stat_value))
    return msg
    
def create_response(sentence, name):
    msg = {}
    if sentence == "test":
        msg = "All systems are go"
    elif sentence == 'wooloo': #Temporarily removes need to use tags.  Bot will respond to everything relevant
        bot_tags.append(' ')
        msg = "Tags removed."
    elif any(word in sentence for word in bot_tags):
        refined = process_sentence(sentence, name)
        if any(word in sentence for word in dnd_stats):
               msg = dnd_stat_calc(refined)
        if 'price' in sentence:
            msg = ge_search(refined)
        if "?" in sentence:
            msg = questions(refined)
        if "roll" in sentence:
            msg = dice_roller(refined)

    time.sleep(.75)
    return msg
       
