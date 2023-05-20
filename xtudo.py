import json

import telebot
from telebot import TeleBot
from telebot import types
from telebot.types import ReplyKeyboardMarkup,ReplyKeyboardRemove

from xtudo_modulo import apaga_mensagem_usuario, apaga_mensagem_bot , mensagem_botao_salva, \
                         apaga_mensagem_usuario_call,mensagem_botao_salva_call,\
                         apaga_mensagem_bot_call,apaga_janela_selecao,mensagem_botao_salva_1botao,\
                         mensagem_botao_salva_1botao_call,delete_all_messages,apaga_mensagem,apaga_mensagem_call, \
                         cria_caixa_selecao,apaga_mensagem_ultima,mensagem_botao_salva_2botoes,mensagem_botao_salva_call_2botoes

from funcao_com_json import lendo_arquivo_json_dic,escrevendo_json_novo

bot=telebot.TeleBot("6218006765:AAF309hpXCmaU1r9P41zKiNK1L8gaqTMyqI")



produtos_preco={}
produto_troca=""


ultima_mensagem_id=None
categoria=""  # servira para armazenar a categoria da de algumas funções
produto=""
valor=""
itens=""
message_ids=[]
categoria_excluida=""

dados=lendo_arquivo_json_dic("loja.json") # Leitura do arquivo json carregando a variável dados







#Mensagem inicial ao escrever algo na tela

@bot.message_handler(func=lambda message: True)
def inicio(message):

      global ultima_mensagem_id
      apaga_mensagem(bot,message)

      markup = types.InlineKeyboardMarkup()  # Criação do teclado menu inicial
      but1 = types.InlineKeyboardButton('Alterar valor do produto e itens', callback_data='alterar')
      but2 = types.InlineKeyboardButton('Criar categoria ou produto', callback_data='criar')
      but3 = types.InlineKeyboardButton('Indisponível: produto ou item', callback_data='indisponivel')
      but4 = types.InlineKeyboardButton('excluir: categoria , produto ou item', callback_data='excluir')
      markup.add(but1)
      markup.add(but2)  # Incorporando os botões
      markup.add(but3)
      markup.add(but4)
      ultima_mensagem_id=mensagem_botao_salva(bot, message, "  Configuração",markup)  # Mensagem com o teclado e a atualização da id da

          # ultima mensagem

#--------------iniciar a exclusão de uma categoria / produto / item------------------------------------------------------
@bot.callback_query_handler(func=lambda call: call.data == 'excluir')
def exclusao(call):
 global ultima_mensagem_id
 apaga_mensagem_call(bot, call)

 keyboard=cria_caixa_selecao(dados)
 ultima_mensagem_id = mensagem_botao_salva_call(bot, call, "Escolha a categoria que será excluida",keyboard)

 bot.register_next_step_handler(call.message, excluir_categoria)

def excluir_categoria(message):

    global ultima_mensagem_id,categoria_excluida
    apaga_mensagem_ultima(bot, message)
    apaga_mensagem(bot, message)
    print(ultima_mensagem_id)

    print("oiq")
    categoria_excluida=message.text #Recebe o que será excluído

    mensagem_botao_salva_2botoes(bot,message,f"Voce confirma a exclusão de: {message.text} ","Sim","Não","sim_excluir","inicio")

@bot.callback_query_handler(func=lambda call: call.data == 'sim_excluir')
def exclusao(call):
    global categoria_excluida
    del dados[categoria_excluida]
    escrevendo_json_novo(dados,"loja.json")
    mensagem_botao_salva_call_2botoes(bot,call,"Excluida com sucesso","Excluir outra","Menu inicial","excluir","inicio")



#--------------iniciar a criação de uma categoria / produto------------------------------------------------------

# pergunta o que quer criar, produto ou categoria
@bot.callback_query_handler(func=lambda call: call.data == 'criar')
def botao_clicado4(call):


     global ultima_mensagem_id
     apaga_mensagem_call(bot,call) # Apaga a mensagem da tela

     markup = telebot.types.InlineKeyboardMarkup()
     bot1= types.InlineKeyboardButton('Categoria', callback_data='cria_categoria')
     bot2 = types.InlineKeyboardButton('Produto', callback_data='cria_produto')
     bot3 =types.InlineKeyboardButton('Retornar', callback_data='inicio')
     markup.add(bot1,bot2,bot3)
     ultima_mensagem_id=mensagem_botao_salva_call(bot,call,"Escolha categoria ou produto",markup)


# Aqui é o momento aonde digitamos o nome da categoria
@bot.callback_query_handler(func=lambda call: call.data == 'cria_categoria')
def botao_clicado1(call):

         global ultima_mensagem_id
         apaga_mensagem_call(bot,call)
         ultima_mensagem_id=mensagem_botao_salva_call(bot,call,"Digite o nome da categoria que deseja criar")
         bot.register_next_step_handler(call.message, adic_categoria) # Avança para uma função determinada independente
                                                                      # da escrita


#Função que cria a categoria
def adic_categoria(message):

    global ultima_mensagem_id
    bot.delete_message(message.chat.id,ultima_mensagem_id)
    apaga_mensagem(bot, message)

    dados[message.text] = None # Aqui eu crio em dados um key com o nome da minha categoria com None
    escrevendo_json_novo(dados,"loja.json")

    markup  = types.InlineKeyboardMarkup()
    botao1 = types.InlineKeyboardButton('continuar criando', callback_data='cria_categoria')
    botao2 = types.InlineKeyboardButton('retornar ao início', callback_data='inicio')
    markup.add(botao1,botao2)
    ultima_mensagem_id=mensagem_botao_salva(bot,message,f"Categoria criada com sucesso: {message.text}",markup)



#Essa função será chamada no momento em que se tenta criar um produto ou um produto sem uma categoria
@bot.callback_query_handler(func=lambda call: call.data == 'cria_produto')
def botao_clicado3(call):
        global ultima_mensagem_id
        apaga_mensagem_call(bot,call)
        if dados == {}: # Caso do loja.json vazio

            markup = telebot.types.InlineKeyboardMarkup()
            botao1 = telebot.types.InlineKeyboardButton('Retorne', callback_data='inicio')
            markup.add(botao1)
            mensagem_botao_salva_call(bot, call, "Você ainda não possui uma categoria cadastrada , "
                                                 "precisa cadastrar uma para adicionar um produto nela", markup)
        else:


            lista = [x for x in dados]  # criação da lista  de categoria
            keyboard = ReplyKeyboardMarkup(
                row_width=1)  # utilizando a lista para criar com os seus itens uma caixa de seleção

            for opcao in lista:
                keyboard.add(opcao)


            ultima_mensagem_id=mensagem_botao_salva_call(bot, call, "Escolha a categoria que deseja incluir seu produto", keyboard)
            bot.register_next_step_handler(call.message, cria_produto_escoha_categoria)

def cria_produto_escoha_categoria(message):

    global ultima_mensagem_id, categoria
    bot.delete_message(message.chat.id, ultima_mensagem_id)
    apaga_mensagem(bot,message)
    categoria = message.text # armazenando valor em categoria para ser usado na proxima função
    ultima_mensagem_id = apaga_janela_selecao(bot, message, "Digite o nome do produto")

    bot.register_next_step_handler(message, digite_produto)
def digite_produto(message):

    global ultima_mensagem_id, produto
    bot.delete_message(message.chat.id, ultima_mensagem_id)
    apaga_mensagem(bot,message)
    produto = message.text # armazenando valor em categoria para ser usado na proxima função

    #apaga_janela_selecao(bot,"Digite o valor do produto")
    ultima_mensagem_id=mensagem_botao_salva(bot, message, "Digite o valor do produto")
    bot.register_next_step_handler(message, digite_valor)
def digite_valor(message):

    global ultima_mensagem_id, valor
    valor = message.text # armazenando valor em categoria para ser usado na proxima função
    bot.delete_message(message.chat.id, ultima_mensagem_id)
    apaga_mensagem(bot,message)
    #apaga_janela_selecao(bot,"Digite os itens do produto")
    ultima_mensagem_id=mensagem_botao_salva(bot, message, "Digite os itens do produto")
    bot.register_next_step_handler(message, digite_itens)
def digite_itens(message):

    global ultima_mensagem_id, itens,dados
    bot.delete_message(message.chat.id, ultima_mensagem_id)
    apaga_mensagem(bot,message)

    itens = message.text # armazenando valor em itens para ser usado
    itens=itens.split()


    markup = telebot.types.InlineKeyboardMarkup()
    botao1 = telebot.types.InlineKeyboardButton('Continuar', callback_data='cria_produto')
    botao2 = telebot.types.InlineKeyboardButton('Menu inicial', callback_data='inicio')
    markup.add(botao1,botao2)

    if dados[categoria]==None: # se for None ele precisa indicar que o proximo elemento é um dic, depois dessa
                               # indicação os demais serão reconhecidos como dic

     dados[categoria]={produto:{"Valor":valor,"Itens":itens}} # Forma para reconhecer como dic

     escrevendo_json_novo(dados,"loja.json")
    else:
     dados[categoria][produto]= {"Valor": valor, "Itens": itens} # Aqui já reconhecido como dic

     escrevendo_json_novo(dados, "loja.json")
    mensagem_botao_salva(bot, message, f"Cadastro:"
                                       f"\nCategoria: {categoria}"
                                       f"\nProduto: {produto}"
                                       f"\nValor: {valor}"
                                       f"\nItens: {itens}"
                                       f"\nPara continuar cadastrando produto clique em continuar",markup)




#----------------------------------fim-------------------------------------------------------------------------




# Chamada pelo final da mudança do valor do produto
@bot.callback_query_handler(func=lambda call: call.data=="inicio")
def inicio(call):

  global ultima_mensagem_id
  apaga_mensagem_call(bot,call)
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
        # Apaga a mensagem que chamou a função
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

  if ultima_mensagem_id !=None:

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


 ultima_mensagem_id = None

 produto_troca=message.text
 markup = ReplyKeyboardRemove(selective=False)
 mensagem=bot.send_message(message.chat.id, "Digite o novo valor desejado:", reply_markup=markup)
 ultima_mensagem_id=mensagem.message_id
 bot.register_next_step_handler(message,produto_valor_final)


def produto_valor_final(message):
    global produto_troca
    global ultima_mensagem_id

  
    produtos_preco[produto_troca]=message.text


    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Retornar ao inicio', callback_data='inicio')
    but2 = types.InlineKeyboardButton('Mudar outro valor', callback_data='produto')
    markup.add(but1, but2)
    mensagem_botao_salva(bot,message,"Operação realizada com sucesso",markup)




bot.polling()
