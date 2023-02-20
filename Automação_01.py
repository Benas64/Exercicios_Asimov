#1.Importar bibliotecas necessárias
import pywhatkit
import keyboard
import time
from datetime import datetime

#2.Definir quais contatos receberão as mensagens
contatos=['+5586999270061','+5586999270062','+5586988291825']
#3.Definir intervalos de envio
while len(contatos)>=1:
    pywhatkit.sendwhatmsg(contatos[0],'VAMOS AUTOMATIZAR TUDO!',datetime.now().hour,datetime.now().minute+2)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
    

