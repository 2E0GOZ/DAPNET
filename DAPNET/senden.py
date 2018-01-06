﻿###############################################################################
# Philipp DL7FL mit unterstuezung von DH3RW (RWTH-AFU)
###############################################################################

import requests
from requests.auth import HTTPBasicAuth
import os

###############################################################################
#  Daten in Variablen Speichern
###############################################################################

# Konstante

login = os.getenv('DAPNET_Benutzer') #  DAPNET Benutzername aus Umgebungsvariablen os.getenv
passwd = os.getenv('DAPNET_Passwort')  #  DAPNET Passwort aus Umgebungsvariablen


url = 'http://www.hampager.de:8080/calls'  #  versenden uebers Internet Variable

text = "test test"  #  Nachrichtentext bis 80 Zeichen  eingeben
rufzeichen = ["dl7fl"]  # eins oder mehrere Emfaenger Rufzeichen
txgroup = "dl-he"  #  Sendergruppe zB. DL-all für alle Sender in Deutschland


###############################################################################
# Funktionen definieren
###############################################################################

def senden(text, callsign, txgroup, login, passwd, url): # json modul
	# print(callsign)
	json_string = '''{"text": "''' + text + '''", "callSignNames": ["''' + callsign + '''"], "transmitterGroupNames": ["''' + txgroup + '''"], "emergency": false}'''
	# print(json_string)
	response = requests.post(url, data=json_string, auth=HTTPBasicAuth(login, passwd)) # Exception handling
	print(response.status_code) # return


def Rufzeichen_vereinzeln(rufzeichen):  #  Rufzeichen vereinzelt und ruft mit jedem Rufzeichen die Senden Funktion auf.
	for callsign in rufzeichen:
		# print(callsign)

		senden(text, callsign, txgroup, login, passwd, url)


Rufzeichen_vereinzeln(rufzeichen)

