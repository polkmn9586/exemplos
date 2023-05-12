
import telebot
from telebot import types

bot=telebot.TeleBot("6218006765:AAF309hpXCmaU1r9P41zKiNK1L8gaqTMyqI")
@bot.message_handler(func=lambda message: True)
def inicio(message):



# Aqui podemos enviar uma mensagem para coletar um dado e enviar esse dado para a função desejada para poder trata-lo
def iniciar_conversa(message):
    bot.send_message(message.chat.id, "texto da mensagem que pode ser usado para pedir um texto")
    bot.register_next_step_handler(message, "nome da função a ser chamada")


# Cria 1 botão com um markup , podendo desse momento em diante fazer ctrl-c ctrl-v dos botões
"markup nome" = telebot.types.InlineKeyboardMarkup()
"botao nome" = telebot.types.InlineKeyboardButton('texto do botão', callback_data='comando dele')
markup.add(botao)


# Atende ao tocar de um botão inline devolvendo uma mensagem de texto podendo ter a indicação para botões
@bot.callback_query_handler(func=lambda call: call.data == 'callback do botão')
def botao_clicado(call):
    bot.answer_callback_query(call.id, text= "texto ao clicar no botão")
    bot.send_message(call.message.chat.id, text= "texto na mensagem", reply_markup="markup")





bot.polling()