
import telebot
import os

TOKEN= '484560229:AAFJLC5DGod2vIH9Bga1mQpMiGWB3s44vic'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	cid = message.chat.id
	bot.send_message(cid, 'Acciones disponibles: \n1)Informacion del bot. \n2)Imprimir mensaje de bienvenida. \n3)Ver enlace GitHub.')

@bot.message_handler(commands=['1'])
def atiende1(message):
	cid = message.chat.id
	archivo = open("README.md")
	texto = archivo.readlines()
	bot.send_message(cid, texto)

@bot.message_handler(commands=['2'])
def atiende2(message):
	cid = message.chat.id
	bot.send_message(cid, 'Bienvenido al bot de JaoChaos para la asignatura de IV.')

@bot.message_handler(commands=['3'])
def atiende3(message):
	cid = message.chat.id
	enlace = 'https://github.com/JaoChaos/Bot_Telegram'
	bot.send_message(cid, enlace)

bot.polling(none_stop=True) # siempre activo
