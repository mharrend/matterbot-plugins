from mattermost_bot.bot import respond_to, listen_to
import os
import pymsgbox
import time
import getpass
import re

@respond_to('MittagessenNun')
@listen_to('MittagessenNun')
def mittagessen_aufruf(message):
    os.system('xdg-open "http://www.aserv.kit.edu/downloads/Speiseplan_deutsch.pdf"')
    time.sleep(3)
    getUserName = getpass.getuser()
    kommtMit = pymsgbox.confirm('Kommst Du mit zum Mittagessen', 'Teilnahme Mittagessen', ["Ja", "Vielleicht", 'Nein'])
    if kommtMit == "Ja":
	message.reply('Ja, %s kommt mit zum Mittagessen' % getUserName)
    elif kommtMit == "Vielleicht":
   	message.reply('Vielleicht kommt %s mit zum Mittagessen' % getUserName)
    else:
        message.reply('%s Kommt nicht mit zum Mittagessen' % getUserName)

mittagessen_aufruf.__doc__ = "Zeigt Speiseplan an und macht Umfrage, wer zum Mittagessen mitkommt"


@respond_to('MittagessenUm (.*)')
@listen_to('MittagessenUm (.*)')
def mittagessen_um(message, uhrzeit):
    getUserName = getpass.getuser()
    kommtMit = pymsgbox.confirm('Kommst Du mit zum Mittagessen um %s' % uhrzeit , 'Teilnahme Mittagessen', ["Ja", "Vielleicht", 'Nein'])
    if kommtMit == "Ja":
        message.reply('Ja, %s kommt mit zum Mittagessen' % getUserName)
    elif kommtMit == "Vielleicht":
        message.reply('Vielleicht kommt %s mit zum Mittagessen' % getUserName)
    else:
        message.reply('%s Kommt nicht mit zum Mittagessen' % getUserName)

mittagessen_um.__doc__ = "Umfrage, wer zu einer bestimmten Zeit zum Mittagessen mitkommt"

@respond_to('SpeiseplanAnzeigen')
@listen_to('SpeiseplanAnzeigen')
def mittagessen_speiseplan(message):
    os.system('xdg-open "http://www.aserv.kit.edu/downloads/Speiseplan_deutsch.pdf"')

mittagessen_speiseplan.__doc__ = "Zeigt Speiseplan an"
