# -*- coding: utf-8 -*-
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
    kommtMit = pymsgbox.confirm(
        'Kommst Du mit zum Mittagessen', 'Teilnahme Mittagessen', [
            "Ja", "Vielleicht", 'Nein'])
    if kommtMit == "Ja":
        message.send(
            'Ja, %s kommt mit zum Mittagessen' %
            getUserName,
            '7iqsqeqaefdmdcy4nj7ccnwfnw')
    elif kommtMit == "Vielleicht":
        message.send('Vielleicht kommt %s mit zum Mittagessen' %
                     getUserName, '7iqsqeqaefdmdcy4nj7ccnwfnw')
    else:
        message.send(
            '%s Kommt nicht mit zum Mittagessen' %
            getUserName,
            '7iqsqeqaefdmdcy4nj7ccnwfnw')

mittagessen_aufruf.__doc__ = "Zeigt Speiseplan an und macht Umfrage, wer zum Mittagessen mitkommt"


@respond_to('MittagessenUm (.*)')
@listen_to('MittagessenUm (.*)')
def mittagessen_um(message, uhrzeit):
    getUserName = getpass.getuser()
    kommtMit = pymsgbox.confirm(
        'Kommst Du mit zum Mittagessen um %s' %
        uhrzeit, 'Teilnahme Mittagessen', [
            "Ja", "Vielleicht", 'Nein'])
    if kommtMit == "Ja":
        message.send(
            'Ja, %s kommt mit zum Mittagessen' %
            getUserName,
            '7iqsqeqaefdmdcy4nj7ccnwfnw')
    elif kommtMit == "Vielleicht":
        message.send('Vielleicht kommt %s mit zum Mittagessen' %
                     getUserName, '7iqsqeqaefdmdcy4nj7ccnwfnw')
    else:
        message.send(
            '%s Kommt nicht mit zum Mittagessen' %
            getUserName,
            '7iqsqeqaefdmdcy4nj7ccnwfnw')

mittagessen_um.__doc__ = "Umfrage, wer zu einer bestimmten Zeit zum Mittagessen mitkommt"


@respond_to('SpeiseplanAnzeigen')
@listen_to('SpeiseplanAnzeigen')
def mittagessen_speiseplan(message):
    # Wichtig, damit nur der ausfuehrende User die Antwort angezeigt bekommt
    if message.get_username() == getpass.getuser():
        os.system(
            'xdg-open "http://www.aserv.kit.edu/downloads/Speiseplan_deutsch.pdf"')

mittagessen_speiseplan.__doc__ = u"Zeigt Speiseplan für einzelnen Benutzer an"
