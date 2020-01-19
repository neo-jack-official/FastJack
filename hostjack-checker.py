#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click    
import sys
import urllib2
import socket
import socks
import time
import requests
#import re
#import json
from urllib2 import urlopen
from colorama import Fore, Back, Style 

web = sys.argv[1]
h = "http://"
fullweb = h + web
ipchecker = 'http://canihazip.com/s'

def check_ip( url, timeout=5 ):
	
    try:
        return urllib2.urlopen(url,timeout=timeout).getcode() == 200
    except urllib2.URLError as e:
        return False
    except socket.timeout as e:
        return False

tor_args = 'NADA'
if len(sys.argv) >= 2:
  try:
      tor_args = sys.argv[2]
      if tor_args == "-T":
        tor = True
      if not tor_args == "-T":
        tor_args = "-F"
        tor = False
  except:      
      tor_args = "-F"
      tor = False

if tor is True:
    ipcheck_url = 'http://canihazip.com/s' 
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050) 
    socket.socket = socks.socksocket
    try:
        tor_ip = requests.get(ipcheck_url) 
        tor_ip = str(tor_ip.text) 
    except requests.exceptions.RequestException as e:
        sys.exit(0)

if tor is False: 
    ipcheck_url2 = 'http://canihazip.com/s' 
    try: 
        regular_ip = requests.get(ipcheck_url2) 
        regular_ip = str(regular_ip.text) 
    except requests.exceptions.RequestException as e:
        sys.exit(0)

print(Fore.RED + Style.BRIGHT + "........................................." + Style.RESET_ALL)
print(Fore.RED + Style.BRIGHT + ".. Instrucciones para HostJack-Checker .." + Style.RESET_ALL)
print(Fore.RED + Style.BRIGHT + ".........................................\n" + Style.RESET_ALL)
print(Back.GREEN + Style.BRIGHT + "Esta APP realiza una peticion cada 9.5 Seg." + Style.RESET_ALL)
print(Back.GREEN + Style.BRIGHT + "Para verificar el estado del servidor (On, Off, TimeOut)" + Style.RESET_ALL)
print("\n")
print(Fore.GREEN + Style.BRIGHT + "Como usar:" + Style.RESET_ALL)
print(Back.MAGENTA + Style.BRIGHT + "/python hostjack-checker.py <web/IP>" + Style.RESET_ALL)
print(Fore.GREEN + Style.BRIGHT + "Ejemplos de Uso de HostJack-Checker:" + Style.RESET_ALL)
print("Sin TOR")
print(Fore.RED + Style.BRIGHT + "Ej.:" +Style.RESET_ALL + Style.BRIGHT + " Python hostjack-checker.py www.ejemplo.com" + Style.RESET_ALL)
print(Fore.RED + Style.BRIGHT + "Ej.:" +Style.RESET_ALL + Style.BRIGHT + " Python hostjack-checker.py www.ejemplo.com -F" + Style.RESET_ALL)
print("Con TOR")
print(Fore.RED + Style.BRIGHT + "Ej.:" +Style.RESET_ALL + Style.BRIGHT + " Python hostjack-checker.py www.ejemplo.com -T" + Style.RESET_ALL)
print("MENU")
print(Fore.RED + Style.BRIGHT + "Ej.:" +Style.RESET_ALL + Style.BRIGHT + " Python hostjack-checker.py -h\n" + Style.RESET_ALL)

if tor is True:
    print(Back.CYAN + Fore.YELLOW + Style.BRIGHT + "Comprobando Informacion TOR ..." + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "Conexion TOR: " + Style.RESET_ALL + Back.GREEN + "Activada" + Style.RESET_ALL)
    try:
        print(Fore.GREEN + Style.BRIGHT + "Nueva Conexion IP-TOR: "+ Style.RESET_ALL + Back.MAGENTA + Fore.YELLOW + Style.BRIGHT + tor_ip + Style.RESET_ALL)
        print(Back.GREEN + Fore.WHITE + Style.BRIGHT + "...... INICIANDO ......" + Style.RESET_ALL)
        
    except requests.exceptions.RequestException as e:
            sys.exit(0)

if tor is False:
    print(Back.CYAN + Fore.YELLOW + Style.BRIGHT + "Comprobando la Informacion que quedara expuesta ..." + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "Conexion TOR: " + Style.RESET_ALL + Back.RED + "Desactivado"+ Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " o " + Style.RESET_ALL + Back.RED + "NO Encontrada" + Style.RESET_ALL)
    ipcheck_url2 = 'http://canihazip.com/s' 
    url = 'http://ipinfo.io/json'
    #response = urlopen(url)
    #data = json.load(response)
    #IP = data['ip']
    #proveedor = data['org']
    #ciudad = data['city']
    #pais = data['country']
    #region = data['region']

    try:
        regular_ip = requests.get(ipchecker) 
        regular_ip = str(regular_ip.text)
        print(Fore.GREEN + Style.BRIGHT + "Tu IP Externa es: "+ Style.RESET_ALL + Back.MAGENTA + Fore.YELLOW + Style.BRIGHT + regular_ip + Style.RESET_ALL)
        #print(Fore.GREEN + Style.BRIGHT + 'La Ubicacion de tu IP es: ' + Style.RESET_ALL + Back.MAGENTA + Fore.YELLOW + Style.BRIGHT + ciudad + ", " + region + ", " + pais + ". " + Style.RESET_ALL)
        #print(Fore.GREEN + Style.BRIGHT + 'Tu Proveedor ISP es: ' + Style.RESET_ALL + Back.MAGENTA + Fore.YELLOW + Style.BRIGHT + proveedor + ". " + Style.RESET_ALL)
        click.confirm('..................... ' + Back.RED + Fore.GREEN + Style.BRIGHT +'Quieres Continuar?' + Style.RESET_ALL, abort=True)
        print(Back.GREEN + Fore.WHITE + Style.BRIGHT + "...... INICIANDO ......" + Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
            sys.exit(0)

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
     print(Fore.GREEN + Style.BRIGHT + 'Servidor %s' %(h) + '%s :' %(web) + Style.RESET_ALL + Back.GREEN + Style.BRIGHT + ' Operando ' + Style.RESET_ALL)
     time.sleep(1)

    if not(check_url(fullweb) == True):
     print(Fore.GREEN + Style.BRIGHT + 'Servidor %s' %(h) + '%s :' %(web) + Style.RESET_ALL + Back.RED + Style.BRIGHT + ' No Disponible ' + Style.RESET_ALL)
     time.sleep(1)

    if(check_url(fullweb) == "TimeOut"):
     print(Fore.GREEN + Style.BRIGHT + 'Servidor %s' %(h) + '%s :' %(web) + Style.RESET_ALL + Back.RED + Fore.YELLOW + Style.BRIGHT + ' No RESPONDE (TimeOut) ' + Style.RESET_ALL)
     time.sleep(1)


