import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup,ReplyKeyboardRemove

from xtudo_modulo import apaga_mensagem_usuario, apaga_mensagem_bot , mensagem_botao_salva, \
                         apaga_mensagem_usuario_call,mensagem_botao_salva_call,\
                         apaga_mensagem_bot_call

bot=telebot.TeleBot("6218006765:AAF309hpXCmaU1r9P41zKiNK1L8gaqTMyqI")





ultima_mensagem_id=None
produtos_preco={}

dados={
        "hambúrguer":{
                       "x-salada":{"valor":10.00,"itens":["batata","molho"]}
                     },
        "cachorro_quente":{
                            "quente_vai":{"valor":10.00,"itens":["batata","molho"]}
                          }

       }
itens=["batata","molho"]
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
    markup.add(but2)# Incorporando os botões
    markup.add(but3)
    markup.add(but4)
    mensagem_botao_salva(bot,message,"  Configuração",markup) # Mensagem com o teclado e a atualização da id da
                                                          # ultima mensagem

  else:  # A repetição da estrutura de cima, quando não há nada salvo na variável última mensagem
      apaga_mensagem_bot(bot,message)

      markup = types.InlineKeyboardMarkup() # Criando o teclado
      but1 = types.InlineKeyboardButton('Alterar valor do produto', callback_data='alterar')
      but2 = types.InlineKeyboardButton('Criar produto ou item', callback_data='criar')
      but3 = types.InlineKeyboardButton('Indisponível: produto ou item', callback_data='indisponivel')
      but4 = types.InlineKeyboardButton('excluir: produto ou item', callback_data='excluir')
      markup.add(but1)
      markup.add(but2)
      markup.add(but3)
      markup.add(but4)
      mensagem_botao_salva(bot,message,"Configuração",markup)











#--------------iniciar a criação de uma categoria / produto------------------------------------------------------

# pergunta o que quer criar
@bot.callback_query_handler(func=lambda call: call.data == 'criar')
def botao_clicado(call):
 global ultima_mensagem_id
 apaga_mensagem_bot_call(bot,call)

 if ultima_mensagem_id!=None:

    markup = telebot.types.InlineKeyboardMarkup()
    bot1= types.InlineKeyboardButton('Categoria', callback_data='cria_categoria')
    bot2 = types.InlineKeyboardButton('Produto', callback_data='cria_produto')
    markup.add(bot1,bot2)

    mensagem=bot.send_message(call.message.chat.id, text= "Deseja criar?", reply_markup=markup)
    ultima_mensagem_id = mensagem.message_id
 else:

     markup = telebot.types.InlineKeyboardMarkup()
     bot1 = types.InlineKeyboardButton('Categoria', callback_data='cria_categoria')
     bot2 = types.InlineKeyboardButton('Produto', callback_data='cria_produto')
     markup.add(bot1, bot2)

     mensagem=bot.send_message(call.message.chat.id, text="Deseja criar?", reply_markup=markup)
     ultima_mensagem_id = mensagem.message_id


# Aqui é o momento aonde digitamos o nome da categoria
@bot.callback_query_handler(func=lambda call: call.data == 'cria_categoria')
def botao_clicado(call):

 global ultima_mensagem_id

 bot.delete_message(call.message.chat.id,ultima_mensagem_id)
 print("o")
 if ultima_mensagem_id!=None:

    mensagem=bot.send_message(call.message.chat.id, text= "Digite o nome da categoria que deseja criar")
    ultima_mensagem_id=mensagem.message_id
    bot.register_next_step_handler(call.message, adic_categoria)
 else:


     mensagem=bot.send_message(call.message.chat.id, text="Digite o nome da categoria que deseja criar")
     ultima_mensagem_id = mensagem.message_id
     bot.register_next_step_handler(call.message, adic_categoria)


#função que cria a categoria
def adic_categoria(message):

    global ultima_mensagem_id

    ultima_mensagem_id=int(ultima_mensagem_id)
    apaga_mensagem_usuario(bot,message)
    bot.delete_message(message.chat.id,ultima_mensagem_id)

    dados[message.text] = None

    markup  = types.InlineKeyboardMarkup()
    botao1 = types.InlineKeyboardButton('continuar criando', callback_data='cria_categoria')
    botao2 = types.InlineKeyboardButton('retornar ao início', callback_data='inicio')
    markup.add(botao1,botao2)

    mensagem_botao_salva(bot,message,"Categoria criada com sucesso",markup)

#----------------------------------fim-------------------------------------------------------------------------




# Chamada pelo final da mudança do valor do produto
@bot.callback_query_handler(func=lambda call: call.data=="inicio")
def inicio(call):

  global ultima_mensagem_id

  apaga_mensagem_usuario_call(bot,call)# Apaga a mensagem que chamou a função

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
    mensagem_botao_salva_call(bot,call,"Configuração",markup)

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
      mensagem_botao_salva_call(bot,call,"Configuração",markup)



# Entra na tela alterar produto ou item
@bot.callback_query_handler(func=lambda call: call.data == 'alterar')
def botao_clicado(call):
  global ultima_mensagem_id
  apaga_mensagem_usuario_call(bot,call)
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
     mensagem_botao_salva_call(bot, call, keyboard, 'Escolha uma opção:')



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
    mensagem_botao_salva(bot,message,"Operação realizada com sucesso",markup)




bot.polling()
