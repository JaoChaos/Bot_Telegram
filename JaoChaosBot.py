
import telebot
import os
import funciones

TOKEN= '484560229:AAFJLC5DGod2vIH9Bga1mQpMiGWB3s44vic'

bot = telebot.TeleBot(TOKEN)
lista=[]
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	cid = message.chat.id
	bot.send_message(cid, 'Acciones disponibles: \n1)Informacion del bot. \n2)Imprimir mensaje de bienvenida. \n3)Ver enlace GitHub. \n4) Despliega menu para rutas.')

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

@bot.message_handler(commands=['4'])
def atiende4(message):
	cid = message.chat.id
	bot.send_message(cid, 'Acciones para rutas: \na) Ver rutas disponibles. \nb)Insertar nueva ruta. \nc)Eliminar ruta.')

@bot.message_handler(commands=['a'])
def atiende_a(message):
	cid = message.chat.id
	funciones.ver_rutas(lista)

@bot.message_handler(commands=['b'])
def atiende_b(message):
	cid = message.chat.id
	ruta=input();
	funciones.insertar_ruta(lista,ruta)
	bot.send_message(cid, 'Se ha insertado la ruta correctamente.')

@bot.message_handler(commands=['c'])
def atiende_c(message):
	cid = message.chat.id
	funciones.eliminar_ruta(lista,ruta)
	bot.send_message(cid, 'Se ha eliminado correctamente la ruta.')

bot.polling(none_stop=True) # siempre activo
