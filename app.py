#Note, this bot was created to respond to a friend in chat who repeats same pictures and phrases

import os
import sys
import json
import random

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))

#############################################
satania = ['https://i.imgur.com/a0c99Xy.jpg', 'http://livedoor.blogimg.jp/goldennews/imgs/9/b/9b99e006.png', 'https://i.imgur.com/CYrJCal.jpg',
           'https://i.ytimg.com/vi/bnkhnX_UIuY/maxresdefault.jpg', 'https://i.ytimg.com/vi/FeMww0y-bI0/hqdefault.jpg', 
           'https://68.media.tumblr.com/53be6ed0e25c44b62897653af23d70d3/tumblr_okywwrfVhq1r5kws5o8_540.jpg'
          ]
           
           
  if data['text'] == '!lasagna':
    num = random.randint(0,len(satania)-1)
    msg = satania[num]
    send_message(msg)
  if data['text'] == 'lasagna':
    msg = 'failure'
    send_message(msg)
  if data['name'] != 'Lunar Bot':
    msg = '{}, you sent "{}".'.format(data['name'], data['text'])
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
