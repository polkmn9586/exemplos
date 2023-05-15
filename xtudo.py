import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup,ReplyKeyboardRemove

from xtudo_modulo import apaga_mensagem_usuario, apaga_mensagem_bot

bot=telebot.TeleBot("6218006765:AAF309hpXCmaU1r9P41zKiNK1L8gaqTMyqI")





ultima_mensagem_id=None
produto = ['x-bacon', 'x-salada']
itens=["batata","molho"]
produtos_itens={produto[0]:[itens[0],itens[1]], produto[1]: [itens[0],itens[1]]}
produtos_preco={produto[0]:10.00, produto[1]:19.00}
produto_troca=""





#Mensagem inicial ao escrever algo na tela
@bot.message_handler(func=lambda message: True)
def inicio(message):
  global ultima_mensagem_id
  apaga_mensagem_usuario(bot,message)
  if ultima_mensagem_id==None:

    markup = types.InlineKeyboardMarkup() #Criação do teclado menu inicial
    but1 = types.InlineKeyboardButton('Alterar valor do produto', callback_data='alterar')
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
      apaga_mensagem_bot(bot,message,ultima_mensagem_id)
      #bot.delete_message(message.chat.id, ultima_mensagem_id)# Deletando id da ultima mensagem
      #ultima_mensagem_id = None

      markup = types.InlineKeyboardMarkup() # Criando o teclado
      but1 = types.InlineKeyboardButton('Alterar valor do produto', callback_data='alterar')
      but2 = types.InlineKeyboardButton('Criar produto ou item', callback_data='criar')
      but3 = types.InlineKeyboardButton('Indisponível: produto ou item', callback_data='indisponivel')
      but4 = types.InlineKeyboardButton('excluir: produto ou item', callback_data='excluir')
      markup.add(but1)
      markup.add(but2)
      markup.add(but3)
      markup.add(but4)
      mensagem = bot.send_message(message.chat.id, text="Configuração:", parse_mode="HTML",reply_markup=markup)
      ultima_mensagem_id = mensagem.message_id # Armazenando a Ultima mensagem para poder apaga-la

# Chamada pelo final da mudança do valor do produto
@bot.callback_query_handler(func=lambda call: call.data=="inicio")
def inicio(call):
  global ultima_mensagem_id
  bot.delete_message(call.message.chat.id, call.message.message_id)# Apaga a mensagem que chamou a função
  if ultima_mensagem_id==None:

    markup = types.InlineKeyboardMarkup() #Criação do teclado menu inicial
    but1 = types.InlineKeyboardButton('Alterar valor do produto ', callback_data='alterar')
    but2 = types.InlineKeyboardButton('Criar produto ou item', callback_data='criar')
    but3 = types.InlineKeyboardButton('Indisponível: produto ou item', callback_data='indisponivel')
    but4 = types.InlineKeyboardButton('excluir: produto ou item', callback_data='excluir')
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    mensagem=bot.send_message(call.message.chat.id,text="  Configuração:\n",parse_mode="HTML",reply_markup=markup)
    ultima_mensagem_id=mensagem.message_id

  else:

      ultima_mensagem_id = None

      markup = types.InlineKeyboardMarkup() # Criando o teclado
      but1 = types.InlineKeyboardButton('Alterar valor do produto', callback_data='alterar')
      but2 = types.InlineKeyboardButton('Criar produto ou item', callback_data='criar')
      but3 = types.InlineKeyboardButton('Indisponível: produto ou item', callback_data='indisponivel')
      but4 = types.InlineKeyboardButton('excluir: produto ou item', callback_data='excluir')
      markup.add(but1)
      markup.add(but2)
      markup.add(but3)
      markup.add(but4)
      mensagem = bot.send_message(call.message.chat.id, text="Configuração:", parse_mode="HTML",reply_markup=markup)
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






@bot.callback_query_handler(func=lambda call: call.data == 'produto')
def botao_clicado(call):
 global ultima_mensagem_id
 if ultima_mensagem_id!=None:
    global produto

    bot.delete_message(call.message.chat.id, ultima_mensagem_id)
    ultima_mensagem_id = None
    keyboard = ReplyKeyboardMarkup(row_width=1)
    for opcao in produtos_preco.keys():
         keyboard.add(opcao)
    mensagem=bot.send_message(call.message.chat.id, 'Escolha uma opção:', reply_markup=keyboard)
    ultima_mensagem_id=mensagem.message_id
    bot.register_next_step_handler(call.message, produto_troca_valor)

 else:

     keyboard = ReplyKeyboardMarkup(row_width=1)
     for opcao in produtos_preco.keys():
         keyboard.add(opcao)
     bot.send_message(call.message.chat.id, 'Escolha uma opção:', reply_markup=keyboard)
     bot.register_next_step_handler(call.message, produto_troca_valor)



def produto_troca_valor(message):
 global produto_troca
 global ultima_mensagem_id
 bot.delete_message(message.chat.id,message.message_id)
 bot.delete_message(message.chat.id, ultima_mensagem_id)
 ultima_mensagem_id = None

 produto_troca=message.text
 markup = ReplyKeyboardRemove(selective=False)
 mensagem=bot.send_message(message.chat.id, "Digite o novo valor desejado:", reply_markup=markup)
 ultima_mensagem_id=mensagem.message_id
 bot.register_next_step_handler(message,produto_valor_final)

def produto_valor_final(message):
    global produto_troca
    global ultima_mensagem_id
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, ultima_mensagem_id)
    ultima_mensagem_id = None
    produtos_preco[produto_troca]=message.text


    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Retornar ao inicio', callback_data='inicio')
    but2 = types.InlineKeyboardButton('Mudar outro valor', callback_data='produto')
    markup.add(but1, but2)
    mensagem=bot.send_message(message.chat.id,"Operação realizada com sucesso",reply_markup=markup)
    ultima_mensagem_id=mensagem.message_id



bot.polling()
