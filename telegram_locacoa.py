import telebot
from telebot import types
import requests


bot=telebot.TeleBot("6218006765:AAF309hpXCmaU1r9P41zKiNK1L8gaqTMyqI") # conexão com o robo telegram


#Primeira mensagem do bot com start ---------------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def iniciar_conversa(message):
 id=message.chat.id
 #Cria o botão de inicio do processo
 markup = telebot.types.InlineKeyboardMarkup()
 but = telebot.types.InlineKeyboardButton('Clique aqui para visualizar dias e horas disponíveis', callback_data='inicio')
 markup.add(but)

 bot.send_message(message.chat.id, "Esse será o nosso intermediador, com ele poderemos tratar das futuras locações",reply_markup=markup)





#quadro 2, tipos de locação --------------------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: call.data == "inicio")
def botao_clicado(call):

    markup1 = telebot.types.InlineKeyboardMarkup()
    but1 = telebot.types.InlineKeyboardButton('Locação única', callback_data='Locacao_unica')
    but2 = telebot.types.InlineKeyboardButton('Locação mensal', callback_data='r')
    but3 = telebot.types.InlineKeyboardButton('↩️ retornar ao ítem anterior', callback_data='inicio')
    markup1.add(but1, but2)
    markup1.add(but3)
    bot.answer_callback_query(call.id, text="Ok , aguarde o próximo passo")
    bot.send_message(call.message.chat.id, text="    Escolha o tipo de locação",reply_markup=markup1)

@bot.callback_query_handler(func=lambda call: call.data == "Locacao_unica")
def botao_clicado(call):

    markup1 = telebot.types.InlineKeyboardMarkup()
    but1 = telebot.types.InlineKeyboardButton('clique para escolha: dia/hora', callback_data='r')
    but2 = telebot.types.InlineKeyboardButton('↩️ retornar ao ítem anterior', callback_data='inicio')
    markup1.add(but1,but2)
    bot.answer_callback_query(call.id, text="Ok , aguarde o próximo passo")
    bot.send_message(call.message.chat.id, text="Nesse tipo de locação será realizada uma locação unitária\n é so clicar a baixo para continuar",reply_markup=markup1)




#mensagem enviada quando se digita um texto qualquer ------------------------------------------------------------
@bot.message_handler(func=lambda message: True)
def inicio(message):
 id = message.chat.id
 markup = telebot.types.InlineKeyboardMarkup()
 but = telebot.types.InlineKeyboardButton('Clique aqui para visualizar dias e horas disponíveis',callback_data='inicio')
 markup.add(but)

 bot.send_message(message.chat.id, "Retornamos a esse ponto devido a mensagem que foi enviada.\nNesse primeiro\
   momento só escolha as opções oferecida na tela do nosso chat",
                   reply_markup=markup)



# 1-mensagem de boas vindas


bot.polling()

# - básico
# A loja será composta por:
#        1-mensagem de boas vindas
#          terá um botão para entrar na escolha dos meses esse botão levará aos dias que ainda não estão ocpados
#        2-escolha do produto principal  botões dos produtos com um de voltar ao ítem anterior
#        3-configuração desse produto
#        4- tela de finalização
# Criar as telas até o pedido final básico
# Gerar a lista e enviar por telegram


# Criar um boot de configuração
  # Boot de estado dos produtos
    # Criar uma lista tendo os produtos para manipulalos
  # Boot de mudança dos produtos

