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

def create_response(sentence, name, parse):
	msg = {}
	if sentence == "test":
		msg = "All systems are go"
	if any(word in sentence for word in bot_tags):
		if "?" in sentence:
			if " or " in sentence:
				seperate_questionmark = sentence.replace('?', ' ?')
				sentence_list = seperate_questionmark.split(" ") #makes each word a list item
				divider_word = sentence_list.index('or')
				choices = [sentence_list[divider_word-1], sentence_list[divider_word+1]]
				selection = random.randint(0,1)
				msg = choices[selection]
			elif any(word in sentence for word in five_ws):
				msg = "Your w words confused me."
			else:
				num = random.randint(0, (len(eight_ball)-1))
				msg = eight_ball[num]
	if "test" in sentence:
		f = open('saved.txt','r')
		message = f.read()
		msg =message
		f.close()
	if "rewrite" in sentence:
		f = open('saved.txt','a')
		f.write('\n' + 'hello world')
		f.close()
		msg = 'Completed'
	time.sleep(1)
	return msg
#https://github.com/PyGithub/PyGithub
