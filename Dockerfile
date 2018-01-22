
FROM ubuntu:16.04
MAINTAINER Juan Anaya Ortiz <juan.anaya.ortiz@correo.ugr.es>

ARG TOKEN_BOT
ENV TOKEN_BOT=$TOKEN_BOT


#Instalamos git
RUN apt-get -y update
RUN apt-get install -y git

#Clonamos el repositorio
RUN git clone https://github.com/JaoChaos/Bot_Telegram


#Instalamos las herramientas de python necesarias
RUN  apt-get -y install python3-setuptools
RUN  apt-get -y install python3-dev
RUN  apt-get -y install build-essential
RUN  apt-get -y install python3-psycopg2
RUN  apt-get -y install libpq-dev
RUN  apt-get -y install python3-pip

#Instalamos los requerimientos necesarios
RUN cd Bot_Telegram && make install

EXPOSE 80
CMD cd Bot_Telegram && ./despliegue.sh
