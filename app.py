#Note, this bot was created to respond to a friend in chat who repeats same pictures and phrases

import os
import sys
import json
import random
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

from database.cat_facts import catfacts
from database.lasagna import lasagna 

negatives = ['cannot', 'not', 'knot', 'annoyed', 'annoy', 'annoying']

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  sentence = data['text']

#############################################
  if data['name'] != 'Satania Bot':
    if "no" in sentence.lower():
           msg = "no u"
           send_message(msg)
    if "911" in data['text']:
            msg = '911'
            send_message(msg)
    if "awoo" in sentence.lower():
           msg = 'awoo'
           send_message(msg)
    if 'fite me' in sentence.lower():
           msg = 'fite me'
           send_message(msg)
  if "league" in sentence.lower():
            msg = 'No'
            send_message(msg)
  if "shut up" in sentence.lower():
      msg = "pls no bulli"
      send_message(msg)
#Commands
  if sentence == '!roll20':
     num = ((random.randint(0,19))+1)
     msg = num
     send_message(msg)
  if sentence == '!lasagna':
    num = random.randint(0,(len(lasagna)-1))
    msg = lasagna[num]
    send_message(msg)
  if sentence == '!catfacts':
    num = random.randint(0, (len(catfacts)-1))
    msg = catfacts[num]
    send_message(msg)


#########################################
  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  
def log(msg):
  print(str(msg))
sys.stdout.flush()
