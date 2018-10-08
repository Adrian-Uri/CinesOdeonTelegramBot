import telebot;
import gets;

TOKEN = 'TOKEN_N'

tb = telebot.TeleBot(TOKEN)

updater=tb.get_updates();
@tb.message_handler(commands=['start'])
def hola(message):
    tb.reply_to(message, "Howdy, how are you doing?")

@tb.message_handler(commands=['lista'])
def hola(message):
    tb.reply_to(message, gets.items())

# @tb.message_handler(func=lambda message: True)
# def echo_all(message):
# 	tb.reply_to(message, message.text)

@tb.message_handler(commands=['add'])
def anadirList(message):
    text = message.text
    texts = text.split(' ')
    cadena=""
    for elemento in texts:
        if elemento!="/add":
            lista.append(elemento)
    for elemento in lista:
        cadena=cadena+elemento+"\n"
    tb.reply_to(message,cadena)

@tb.message_handler(commands=['del'])
def borrarList(message):
    text = message.text
    texts = text.split(' ')
    cadena=""
    for elemento in texts:
        if elemento!="/del":
            lista.remove(elemento)
    for elemento in lista:
        cadena = cadena + elemento + "\n"
    tb.reply_to(message, cadena)

@tb.message_handler(commands=['gente'])
def imprimeGente(message):
    cadena=""
    for elemento in lista:
        cadena = cadena + elemento + "\n"
    tb.reply_to(message, cadena)


lista=list()
tb.polling()