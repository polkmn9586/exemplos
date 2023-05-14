import telebot
from telebot import types
import time

bot=telebot.TeleBot("6218006765:AAF309hpXCmaU1r9P41zKiNK1L8gaqTMyqI")
ultima_mensagem_id=None

##Cria uma receptor que receberá qualquer mensagem digitada

ultima_mensagem_id=None
chatt_id=None

#Mensagem inicial ao escrever algo na tela
@bot.message_handler(func=lambda message: True)
def inicio(message):
  global ultima_mensagem_id
  if ultima_mensagem_id==None:

    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Alterar produto ou item', callback_data='alterar')
    but2 = types.InlineKeyboardButton('Criar produto ou item', callback_data='criar')
    but3 = types.InlineKeyboardButton('Indisponível: produto ou item', callback_data='indisponivel')
    but4 = types.InlineKeyboardButton('excluir: produto ou item', callback_data='excluir')
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    mensagem=bot.send_message(message.chat.id,text="  Configuração:\n",parse_mode="HTML",reply_markup=markup)
    ultima_mensagem_id=mensagem.message_id

  else:
      bot.delete_message(message.chat.id, ultima_mensagem_id)
      ultima_mensagem_id = None

      markup = types.InlineKeyboardMarkup()
      but1 = types.InlineKeyboardButton('Alterar produto ou item', callback_data='alterar')
      but2 = types.InlineKeyboardButton('Criar produto ou item', callback_data='criar')
      but3 = types.InlineKeyboardButton('Indisponível: produto ou item', callback_data='indisponivel')
      but4 = types.InlineKeyboardButton('excluir: produto ou item', callback_data='excluir')
      markup.add(but1)
      markup.add(but2)
      markup.add(but3)
      markup.add(but4)
      mensagem = bot.send_message(message.chat.id, text="Configuração:", parse_mode="HTML",
                                  reply_markup=markup)
      ultima_mensagem_id = mensagem.message_id



# Entra na tela alterar produto ou item
@bot.callback_query_handler(func=lambda call: call.data == 'alterar')
def botao_clicado(call):
  global ultima_mensagem_id
  if ultima_mensagem_id !=None:

    bot.delete_message(call.message.chat.id, ultima_mensagem_id)
    ultima_mensagem_id=None
    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Produto', callback_data='produto')
    but2 = types.InlineKeyboardButton('Item', callback_data='item')
    but3 = types.InlineKeyboardButton('Voltar', callback_data='voltar')

    markup.add(but1)
    markup.add(but2)
    markup.add(but3)

    bot.answer_callback_query(call.id, text="texto ao clicar no botão")
    mensagem=bot.send_message(call.message.chat.id, text="Modificação", reply_markup=markup)
    ultima_mensagem_id=mensagem.message_id
  else:
      markup = types.InlineKeyboardMarkup()
      but1 = types.InlineKeyboardButton('Produto', callback_data='produto')
      but2 = types.InlineKeyboardButton('Item', callback_data='item')
      but3 = types.InlineKeyboardButton('Voltar', callback_data='voltar')
      bot.answer_callback_query(call.id, text="texto ao clicar no botão")

      markup.add(but1)
      markup.add(but2)
      markup.add(but3)

      mensagem=bot.send_message(call.message.chat.id, text="Modificação", reply_markup=markup)
      ultima_mensagem_id = mensagem.message_id




bot.polling()
