# -*-coding:Latin-1 -*

from slackbot.bot import respond_to
from slackbot.bot import listen_to

import re

@listen_to('(.*)gratt(.*)', re.IGNORECASE)
def gratter(message, before='', after=''):
    message.reply(format(before) + 'trait' + format(after), in_thread=True)

@listen_to('(.*)trait(.*)', re.IGNORECASE)
def traiter(message, before='', after=''):
    message.reply(format(before) + 'gratt' + format(after), in_thread=True)

@listen_to('(.*)copine(.*)', re.IGNORECASE)
def Villefranche(message, before='', after=''):
    message.reply(format(before) + 'Villefranche' + format(after), in_thread=True)

@listen_to('(.*)villefranche(.*)', re.IGNORECASE)
def copine(message, before='', after=''):
    message.reply(format(before) + 'copine' + format(after), in_thread=True)
