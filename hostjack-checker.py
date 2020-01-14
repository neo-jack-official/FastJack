#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click    ###3 para Yes o no continue
import sys
import urllib2
import socket
import time
import requests
from urllib2 import urlopen
import re
import json
from datetime import date, datetime
from colorama import Fore, Back, Style ## dar Color a INFO

########### Variables

web = sys.argv[1]
#web = "www.ejemplo.cl"
h = "http://"
fullweb = h + web
fecha = date.today()
ahora = datetime.now()
hora = ahora.strftime("%H:%M:%S")
ipchecker = 'http://canihazip.com/s'

###########
######################################### HOST CHEKER MAIN
def check_ip( url, timeout=5 ):
	
    try:
        return urllib2.urlopen(url,timeout=timeout).getcode() == 200
    except urllib2.URLError as e:
        return False
    except socket.timeout as e:
        return False

######################################
print Fore.RED + Style.BRIGHT + ".........................................\n" + Style.RESET_ALL
print Back.GREEN + Style.BRIGHT + "Esta APP realiza una peticion cada 9.5 Seg." + Style.RESET_ALL
print Back.GREEN + Style.BRIGHT + "Para verificar el estado del servidor (On, Off, TimeOut)" + Style.RESET_ALL
print Fore.RED + Style.BRIGHT + ".........................................\n" + Style.RESET_ALL
print Fore.RED + Style.BRIGHT + ".........................................\n" + Style.RESET_ALL
print Fore.YELLOW + Style.BRIGHT + "Esta version de HostJack-Checker, NO USA TOR" + Style.RESET_ALL
print Fore.YELLOW + Style.BRIGHT + "SIEMPRE UTILICE UNA VPN." + Style.RESET_ALL
print Fore.YELLOW + Style.BRIGHT + "De lo contrario, su identidad puede quedar expuesta..\n" + Style.RESET_ALL
print Back.CYAN + Fore.YELLOW + Style.BRIGHT + "Comprobando la Informacion que quedara expuesta ..." + Style.RESET_ALL 
regular_ip = requests.get(ipchecker) # variable envia peticion a la web que da ip
regular_ip = str(regular_ip.text) # la combierte a texto
print Fore.GREEN + Style.BRIGHT + "Conexion TOR: " + Style.RESET_ALL + Back.RED + "Desactivado"+ Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " o " + Style.RESET_ALL + Back.RED + "NO Encontrada" + Style.RESET_ALL

print Fore.GREEN + Style.BRIGHT + "Tu IP Externa es: "+ Style.RESET_ALL + Back.MAGENTA + Fore.YELLOW + Style.BRIGHT + regular_ip + Style.RESET_ALL

################## Rastrear Ubicacion
#from urllib2 import urlopen
#import re
#import json
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP = data['ip']
proveedor = data['org']
ciudad = data['city']
pais = data['country']
region = data['region']

print Fore.GREEN + Style.BRIGHT + 'La Ubicacion de tu IP es: ' + Style.RESET_ALL + Back.MAGENTA + Fore.YELLOW + Style.BRIGHT + ciudad + ", " + region + ", " + pais + ". " + Style.RESET_ALL
print Fore.GREEN + Style.BRIGHT + 'Tu Proveedor ISP es: ' + Style.RESET_ALL + Back.MAGENTA + Fore.YELLOW + Style.BRIGHT + proveedor + ". " + Style.RESET_ALL
#####################3

############################# SI O NO
click.confirm('..................... ' +Back.RED + Fore.GREEN + Style.BRIGHT +'Quieres Continuar?' + Style.RESET_ALL, abort=True)
######################################


while True:

    def check_url( url, timeout=5 ):
          try:
              return urllib2.urlopen(url,timeout=timeout).getcode() == 200
          except urllib2.URLError as e:
              return False
          except socket.timeout as e:
              return "TimeOut"
          except Exception:
              pass

    time.sleep(1.5)
    if(check_url(fullweb) == True):
     print fecha, hora, Fore.GREEN + Style.BRIGHT +"Servidor %s" %(h) + "%s :" %(web) + Style.RESET_ALL + Back.GREEN + Style.BRIGHT + " Operando " + Style.RESET_ALL
     time.sleep(1)

    if not(check_url(fullweb) == True):
     print fecha, hora, Fore.GREEN + Style.BRIGHT +"Servidor %s" %(h) + "%s :" %(web) + Style.RESET_ALL + Back.RED + Style.BRIGHT + " No Disponible " + Style.RESET_ALL
     time.sleep(1)

    #if(check_url(fullweb) != True or False):
    if(check_url(fullweb) == "TimeOut"):
     print fecha, hora, Fore.GREEN + Style.BRIGHT +"Servidor %s" %(h) + "%s :" %(web) + Style.RESET_ALL + Back.RED + Fore.YELLOW + Style.BRIGHT + " No RESPONDE (TimeOut) " + Style.RESET_ALL
     time.sleep(1)



