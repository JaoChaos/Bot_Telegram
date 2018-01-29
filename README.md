# Bot_Telegram
## Bot de Telegram para la asignatura IV.

JaoChaosBot es un bot de telegram muy sencillo. Básicamente se encarga de recibir un comando para bash de linux y se encarga de ejecutarlo remotamente en tu pc. Es una buena forma de poder trabajar en el ordenador de tu casa mientras estás fuera.

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
