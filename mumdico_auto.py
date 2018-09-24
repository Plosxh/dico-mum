# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from slackbot.bot import respond_to
from slackbot.bot import listen_to

import re
import json
import io
import requests
import boto3
import os

url = 'http://mum-dico.s3-website-eu-west-1.amazonaws.com/translate.json'

resp = requests.get(url=url)
data = resp.json()
print(data)

@listen_to('(.*)', re.IGNORECASE)
def auto(message, text=''):
    
    for item in data:
        text = text.encode('utf-8')
        replace_word = re.compile(item["word"], re.IGNORECASE)
        new_text = replace_word.sub(item["trad"], text)

    if new_text != text:
        message.reply(format('> ' + new_text), in_thread=True)
        message.react('face_with_monocle')

@respond_to('ajoute (.*) (.*)', re.IGNORECASE)
def ajoute(message, word='', trad=''):
    dic = { "word": word.encode('utf-8'), "trad": trad.encode('utf-8') }
    dic_reverse = { "word": trad.encode('utf-8'), "trad": word.encode('utf-8') }
    data.append(dic)
    data.append(dic_reverse)

    with open('translate.json', 'w') as outfile:
        json.dump(data, outfile)

    translate = open('translate.json', 'rb')

    session = boto3.Session(
        aws_access_key_id=os.environ['ACCESS_KEY'],
        aws_secret_access_key=os.environ['SECRET_KEY']
    )
    s3 = session.resource('s3')
    s3.Bucket('mum-dico').put_object(Key='translate.json', Body=translate)

    message.reply('J\'ai ajouté le mot "' + format(word) + '" et sa traduction "' + format(trad) + '"', in_thread=True)
    message.react('+1')