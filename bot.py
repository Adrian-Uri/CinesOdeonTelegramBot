import telebot;
import gets;

TOKEN = 'TOKEN_N'

tb = telebot.TeleBot(TOKEN)

updater=tb.get_updates();
@tb.message_handler(commands=['start'])
def hola(message):
    tb.reply_to(message, "Howdy, how are you doing?")

@tb.message_handler(commands=['lista'])
def printlista(message):
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
        if elemento not in lista:
            if elemento!="/add":
                lista.append(elemento)
        else:
            tb.reply_to(message, "Si " + elemento + " ya viene, pa que le invitan")
    for elemento in lista:
        cadena=cadena+elemento+"\n"
    if(cadena):
        tb.reply_to(message,cadena)
    else:
        tb.send_message(message.chat.id,"Lista vacia, usame como \"/add nombre1 nombre2\".")

@tb.message_handler(commands=['del'])
def borrarList(message):
    text = message.text
    texts = text.split(' ')
    cadena=""
    for elemento in texts:
        if elemento!="/del":
            if elemento in lista:
                lista.remove(elemento)
            else:
                tb.reply_to(message, "Hijo de puta, "+elemento+" no existe")
    for elemento in lista:
        cadena = cadena + elemento + "\n"
    if (cadena):
        tb.reply_to(message, cadena)
    else:
        tb.send_message(message.chat.id, "No va ni peter")

@tb.message_handler(commands=['gente'])
def imprimeGente(message):
    cadena=""
    for elemento in lista:
        cadena = cadena + elemento + "\n"
    tb.reply_to(message, cadena)


lista=list()
tb.polling()