
import telebot
from telebot import types

bot=telebot.TeleBot("6218006765:AAF309hpXCmaU1r9P41zKiNK1L8gaqTMyqI")

##Cria uma receptor que receberá qualquer mensagem digitada e retornará uma mensagem com um botão como padrão.
#Utilizada geralmente para mensagem inicial.
# podendo ser alterada a quantidade de botões adicionando mais.
# Aqui ultima_mensagem já recebendo a id da ultima mensagem

ultima_mensagem_id=None
@bot.message_handler(func=lambda message: True)
def inicio(message):
    global ultima_mensagem_id
    if ultima_mensagem_id == None:
        markup = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton('Texto da mensagem', callback_data='indicador call')
        markup.add(but1)
        mensagem=bot.send_message(message.chat.id, text="Texdo da mensagem", reply_markup=markup) # lembrando que text não pode estar vazio
        ultima_mensagem_id=mensagem.message_id
    else:
        bot.delete_message(message.chat.id, ultima_mensagem_id)
        ultima_mensagem = None

        markup = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton('Texto da mensagem', callback_data='indicador call')
        markup.add(but1)
        mensagem = bot.send_message(message.chat.id, text="Texdo da mensagem",reply_markup=markup)  # lembrando que text não pode estar vazio
        ultima_mensagem_id = mensagem.message_id


...
# Aqui podemos enviar uma mensagem para coletar um dado e enviar esse dado para a função desejada para poder trata-lo
def iniciar_conversa(message):
    bot.send_message(message.chat.id, "texto da mensagem que pode ser usado para pedir um texto")
    bot.register_next_step_handler(message, "nome da função a ser chamada")


# Cria 1 botão com um markup , podendo desse momento em diante fazer ctrl-c ctrl-v dos botões
"markup nome" = telebot.types.InlineKeyboardMarkup()
"botao nome" = telebot.types.InlineKeyboardButton('texto do botão', callback_data='comando dele')
markup.add(botao)


# Atende ao tocar de um botão inline devolvendo uma mensagem de texto podendo ter a indicação para botões.
# Lembrando que aqui dentro já temos a ultima_mensagem para podermos excluir
@bot.callback_query_handler(func=lambda call: call.data == 'callback do botão')
def botao_clicado(call):
 global ultima_mensagem_id

 if ultima_mensagem_id!=None:

    bot.delete_message(call.message.chat.id,ultima_mensagem_id)
    ultima_mensagem=None
    bot.answer_callback_query(call.id, text= "texto ao clicar no botão")
    mensagem=bot.send_message(call.message.chat.id, text= "texto na mensagem", reply_markup="markup")
    ultima_mensagem=mensagem.message_id
 else:
     
     bot.answer_callback_query(call.id, text="texto ao clicar no botão")
     mensagem=bot.send_message(call.message.chat.id, text="texto na mensagem", reply_markup="markup")
     ultima_mensagem = mensagem.message_id


#Apagando a ultima mensagem colocada na tela. Ele trabalha com uma variável externa que armazena valores










bot.polling()