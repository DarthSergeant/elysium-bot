import os
import sys
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

from database.ai import create_response

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  name = data['name']
  parse = data['text']
  sentence = parse.lower()
  response = create_response(sentence, name)
  if response:
    if data['name'] != "Elysia":
      send_message(response)
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
