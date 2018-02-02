# Bot_Telegram
## Bot de Telegram para la asignatura IV.

JaoChaosBot es un bot de telegram muy sencillo. Básicamente recibe un comando para bash de linux y se encarga de ejecutarlo remotamente en tu pc. Es una buena forma de poder trabajar en el ordenador de tu casa mientras estás fuera.

Para usarlo solo es necesario tener instalado Telegram en tu pc y en tu móvil y dejar el pc encendido con telegram abierto  cuando estás fuera. De ésta forma, con el móvil podrás crear ficheros, cambiar entre carpetas, listar los ficheros que hay en tu pc, copiar, mover y eliminar archivos, y mil cosas más.

## Integración continua:
Como herramienta de integración continua he usado Travis, que junto a la libreria "unittest" de python constituyen una poderosa herramienta open-source para desarrollar tests unitarios y mantener la integración continua en proyectos basados en Python.

[![Build Status](https://travis-ci.org/JaoChaos/Bot_Telegram.svg?branch=master)](https://travis-ci.org/JaoChaos/Bot_Telegram)

## Despliegue como PaaS (Platform as a Service):
Como herramienta para desplegar el servivio como plataforma he usado Heroku, una herramienta que a pesar de ser libre ofrece una gran amplitud de herramientas para el despliegue de servicios.

Despliegue https://jaochaosbot.herokuapp.com/

## Pruebas en contenedores aislados:
Para realizar las pruebas antes de lanzar el servicio he usado el ya conocido por todos Docker, que debido a su popularidad y a su fácil uso se ha convertido en una de las herramientas más utilizadas para ese fin.

Enlace a [DockerHub](https://hub.docker.com/r/jaochaos/bot_telegram/) .

## Despliegue en Zeit:

Contenedor: https://bottelegram-ycujievwcq.now.sh

## Despliegue en una máquina virtual:

Para este propósito he elegido "Azure", puesto que al ser una herramienta de pago ofrece muchas posibilidades y he obtenido una licencia gratuita gracias al profesor de la asignatura.

Para ello he instalado la herramienta:

```sh
$ sudo npm install -g azure-cli
```

Después de la instalación y la [configuración](https://unindented.org/articles/provision-azure-boxes-with-vagrant/) de la máquina, instalamos la herramienta "Ansible" para aprovisionar nuestra máquina y creamos los ficheros necesarios para que funcione.

Después de ello, solo nos queda crear el [fichero que configura Vagrant](https://github.com/JaoChaos/Bot_Telegram/blob/master/Vagrantfile) y crear el fichero de despliegue con la herramienta "fabric" : [Fabfile.py](https://github.com/JaoChaos/Bot_Telegram/blob/master/despliegue/fabfile.py).

Para acabar, subimos la máquina a la nube y comprobamos que todo funciona correctamente.
En mi caso, he creado un [archivo](https://github.com/JaoChaos/Bot_Telegram/blob/master/scripts/deploying.sh) para desplegar automáticamente la máquina.

## Despliegue final con Vagrant, ansible y fabric en la cloud de Azure:

Despliegue final: jaochaosbot.southcentralus.cloudapp.azure.com
