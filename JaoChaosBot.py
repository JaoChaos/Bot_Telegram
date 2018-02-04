#!/usr/bin/env python3
import telebot
import time
import urllib
import subprocess
from telebot import types
import os

TOKEN = '484560229:AAFJLC5DGod2vIH9Bga1mQpMiGWB3s44vic'

bot = telebot.TeleBot(TOKEN)
tiempo = time.strftime("%H horas %M minutos y %S segundos exactamente")


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    cid = message.chat.id
    bot.send_message(
        cid,
        'Acciones disponibles: \n1)Informacion del bot. \n2)Imprimir mensaje de bienvenida. \n3)Ver enlace GitHub. \nstart) Escribe comando.'
    )


@bot.message_handler(commands=['1'])
def atiende1(message):
    cid = message.chat.id
    archivo = open("README.md")
    texto = archivo.readlines()
    bot.send_message(cid, texto)


@bot.message_handler(commands=['2'])
def atiende2(message):
    cid = message.chat.id
    bot.send_message(cid,
                     'Bienvenido al bot de JaoChaos para la asignatura de IV.')


@bot.message_handler(commands=['3'])
def atiende3(message):
    cid = message.chat.id
    enlace = 'https://github.com/JaoChaos/Bot_Telegram'
    bot.send_message(cid, enlace)


@bot.message_handler(commands=['start'])
def send_photo(message):
    bot.send_message(message.chat.id, 'Type')


def recibe(messages):
    for m in messages:
        if m.content_type == "text":
            ok = subprocess.call(
                'echo \"' + m.text + '\" >> archivoSalida', shell=True)
            if ok == 0:
                archivo = open('archivoSalida', 'r+')
                archivo.write('OK')
                show = archivo.read()
                subprocess.call('rm archivoSalida', shell=True)
                bot.send_message(m.chat.id, show + "ok")

            else:
                bot.send_message(m.chat.id, "Error")


bot.set_update_listener(recibe)

bot.polling()

bot.polling(none_stop=True)  # siempre activo
