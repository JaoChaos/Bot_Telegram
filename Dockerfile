FROM python:3.6
MAINTAINER Juan Anaya Ortiz <juan.anaya.ortiz@correo.ugr.es>

ARG TOKEN_BOT
ENV TOKEN_BOT=$TOKEN_BOT
ENV PORT=80

RUN mkdir -p /usr/src/app
COPY . /usr/src/app/
WORKDIR /usr/src/app/

#Instalamos los requerimientos necesarios
RUN make install

EXPOSE 80
CMD ["python", "web.py"]
