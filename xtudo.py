import json

import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup,ReplyKeyboardRemove

from xtudo_modulo import apaga_mensagem_usuario, apaga_mensagem_bot , mensagem_botao_salva, \
                         apaga_mensagem_usuario_call,mensagem_botao_salva_call,\
                         apaga_mensagem_bot_call,apaga_janela_selecao
from funcao_com_json import lendo_arquivo_json_dic,escrevendo_json_novo

bot=telebot.TeleBot("6218006765:AAF309hpXCmaU1r9P41zKiNK1L8gaqTMyqI")



produtos_preco={}
produto_troca=""


ultima_mensagem_id=None
categoria=""  # servira para armazenar a categoria da de algumas funções
produto=""
valor=""
itens=""


dados=lendo_arquivo_json_dic("loja.json") # Leitura do arquivo json carregando a variável dados




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

 bot.delete_message(call.message.chat.id,ultima_mensagem_id) # deletando mensagem da tela

 if ultima_mensagem_id!=None:

    mensagem=bot.send_message(call.message.chat.id, text= "Digite o nome da categoria que deseja criar")
    ultima_mensagem_id=mensagem.message_id
    bot.register_next_step_handler(call.message, adic_categoria)
 else:


     mensagem=bot.send_message(call.message.chat.id, text="Digite o nome da categoria que deseja criar")
     ultima_mensagem_id = mensagem.message_id
     bot.register_next_step_handler(call.message, adic_categoria)



@bot.callback_query_handler(func=lambda call: call.data == 'cria_produto')
def botao_clicado(call):

 global ultima_mensagem_id

 bot.delete_message(call.message.chat.id,ultima_mensagem_id) # deletando mensagem da tela
 if dados=={}:
     markup = telebot.types.InlineKeyboardMarkup()
     botao1 = telebot.types.InlineKeyboardButton('Retorne', callback_data='inicio')
     markup.add(botao1)
     mensagem_botao_salva_call(bot,call,"Você ainda não possui uma categoria cadastrada , "
                                        "precisa cadastrar uma para adicionar um produto nela",markup)
 else:
     if ultima_mensagem_id!=None: # executando caso o id da última_mensagem esteja vazio

        lista = [x for x in dados] # criação da lista  de categoria

        keyboard = ReplyKeyboardMarkup(row_width=1) # utilizando a lista para criar com os seus itens uma caixa de seleção
        for opcao in lista:
            keyboard.add(opcao)

        mensagem_botao_salva_call(bot,call,"Escolha a categoria que deseja incluir seu produto",keyboard)
        bot.register_next_step_handler(call.message,cria_produto_escoha_categoria )
     else:
         lista = [x for x in dados]  # criação da lista  de categoria
         keyboard = ReplyKeyboardMarkup(
             row_width=1)  # utilizando a lista para criar com os seus itens uma caixa de seleção
         for opcao in lista:
             keyboard.add(opcao)
         mensagem_botao_salva_call(bot, call, "Escolha a categoria que deseja incluir seu produto",keyboard)
         bot.register_next_step_handler(call.message,cria_produto_escoha_categoria )




#função que cria a categoria
def adic_categoria(message):

    global ultima_mensagem_id

    ultima_mensagem_id=int(ultima_mensagem_id)
    apaga_mensagem_usuario(bot,message)
    bot.delete_message(message.chat.id,ultima_mensagem_id)

    dados[message.text] = None # Aqui eu crio em dados um key com o nome da minha categoria com None
    escrevendo_json_novo(dados,"loja.json")

    markup  = types.InlineKeyboardMarkup()
    botao1 = types.InlineKeyboardButton('continuar criando', callback_data='cria_categoria')
    botao2 = types.InlineKeyboardButton('retornar ao início', callback_data='inicio')
    markup.add(botao1,botao2)

    mensagem_botao_salva(bot,message,"Categoria criada com sucesso",markup)



def cria_produto_escoha_categoria(message):

    global ultima_mensagem_id, categoria
    categoria = message.text # armazenando valor em categoria para ser usado na proxima função

    apaga_mensagem_bot(bot,message)
    apaga_mensagem_usuario(bot, message)

    #apaga_janela_selecao(bot,"Digite o nome do produto")
    #print("oi")
    mensagem_botao_salva(bot,message,"Digite o nome do produto")
    bot.register_next_step_handler(message, digite_produto)

def digite_produto(message):

    global ultima_mensagem_id, produto
    produto = message.text # armazenando valor em categoria para ser usado na proxima função

    apaga_mensagem_bot(bot,message)
    apaga_mensagem_usuario(bot, message)

    #apaga_janela_selecao(bot,"Digite o valor do produto")
    mensagem_botao_salva(bot, message, "Digite o valor do produto")
    bot.register_next_step_handler(message, digite_valor)

def digite_valor(message):

    global ultima_mensagem_id, valor
    valor = message.text # armazenando valor em categoria para ser usado na proxima função

    apaga_mensagem_bot(bot,message)
    apaga_mensagem_usuario(bot, message)

    #apaga_janela_selecao(bot,"Digite os itens do produto")
    mensagem_botao_salva(bot, message, "Digite os itens do produto")
    bot.register_next_step_handler(message, digite_itens)

def digite_itens(message):

    global ultima_mensagem_id, itens,dados
    itens = message.text # armazenando valor em itens para ser usado
    itens=itens.split()
    apaga_mensagem_bot(bot,message)
    apaga_mensagem_usuario(bot, message)

    if dados[categoria]==None: # se for None ele precisa indicar que o proximo elemento é uma lista, depois dessa
                               # indicação os demais serão reconhecidos como lista

     dados[categoria]={produto:{"Valor":valor,"Itens":itens}} # Forma para reconhecer como lista

    else:
     dados[categoria][produto]= {"Valor": valor, "Itens": itens} # Aqui já reconhecido como lista


    mensagem_botao_salva(bot, message, "Digite os itens do produto")
    bot.register_next_step_handler(message, digite_itens)



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
