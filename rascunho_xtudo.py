
import json

import telebot
from telebot import TeleBot
from telebot import types
from telebot.types import ReplyKeyboardMarkup,ReplyKeyboardRemove, InlineKeyboardMarkup,InlineKeyboardButton

from xtudo_modulo import apaga_mensagem_usuario, apaga_mensagem_bot , mensagem_botao_salva, \
                         apaga_mensagem_usuario_call,mensagem_botao_salva_call,\
                         apaga_mensagem_bot_call,apaga_janela_selecao,mensagem_botao_salva_1botao,\
                         mensagem_botao_salva_1botao_call,delete_all_messages,apaga_mensagem,apaga_mensagem_call, \
                         cria_caixa_selecao,mensagem_botao_salva_2botoes,mensagem_botao_salva_call_2botoes,\
                         mensagem_botao_salva_call_3botoes,cria_caixa_selecao_com_1opcao,cria_caixa_selecao_com_2opcao,apaga_mensagem_id\
                         ,apaga_mensagem_id_call

from funcao_com_json import lendo_arquivo_json_dic,escrevendo_json_novo , adiciona_elemento_na_lista_json ,\
                            lendo_arquivo_json_

bot=telebot.TeleBot("6218006765:AAF309hpXCmaU1r9P41zKiNK1L8gaqTMyqI")

# Carregar o arquivo loja.json
with open('loja.json') as file:
    loja_data = json.load(file)

with open("itens.json") as file:
    itens= json.load(file)





#---------------------------criar funções com as categorias produtos e itens--------------------------------

def lista_categorias():
    categorias=loja_data.keys()
    return categorias
def lista_produtos(categoria,chat_id):
    produtos={chat_id:loja_data.get(categoria,{}).keys()}

    return produtos[chat_id]

def lista_itens(categoria,produto):
    itens=loja_data[categoria][produto].get("Itens",[])
    return itens

categorias=lista_categorias()


#---------------------------Fim da criação das funções com as categorias produtos e itens--------------------------------

#---------------------------mensagem inicial -------------------------------------------------------------------------
@bot.message_handler(func=lambda message: True)
def inicio(message):
    mensagem= message.message_id
    chat=message.chat.id

    markup= telebot.types.InlineKeyboardMarkup(row_width=1)
    botao=telebot.types.InlineKeyboardButton("Fazer um pedido",callback_data="pedido")
    markup.add(botao)
    bot.send_message(message.chat.id, " Seja bem vindo a nossa loja",reply_markup=markup)
    for x in range(mensagem,mensagem-5,-1):
       try:
        bot.delete_message(chat,x)
       except:
           pass

#-------------------------------Escolha da categoria em que está o produto-----------------------------------------------

@bot.callback_query_handler(func= lambda call: call.data == "pedido")
def escolha_categoria(call):

    mensagem = call.message.message_id
    chat = call.message.chat.id



    markup=telebot.types.InlineKeyboardMarkup(row_width=1)
    for x in categorias:
     botao=telebot.types.InlineKeyboardButton(x,callback_data=x)
     markup.add(botao)
    bot.send_message(chat,"Escolha a categoria do produto", reply_markup=markup )
    for x in range(mensagem, mensagem - 5, -1):
        try:
            bot.delete_message(chat, x)
        except:
            pass


categoria_escolhida={} # dicionário criado com a categoria escolhida pelo cliente
produtos_da_categoria={} # dicionario criado com o id do cliente mais a lista de produtos da categoria escolhida

# Aqui ocorrerá a escolha do produto
@bot.callback_query_handler(func= lambda call: call.data in categorias)
def escolha_produtos(call):
    global categoria_escolhida ,produtos_da_categoria
    mensagem = call.message.message_id
    chat = call.message.chat.id

    categoria_escolhida[chat]=call.data
    produtos_da_categoria=lista_produtos(call.data,chat)

    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    for x in produtos_da_categoria:
        botao = telebot.types.InlineKeyboardButton(x, callback_data=x)
        markup.add(botao)
    bot.send_message(chat, "Escolha o produto", reply_markup=markup)
    for x in range(mensagem, mensagem - 5, -1):
        try:
            bot.delete_message(chat, x)
        except:
            pass

dicionario_itens_produto={} # listará os itens do produto  escolhidos pelo cliene
lista_itens_produto1=[] # lista dos itens escolhidos


# Aqui , com o produto já escolhido ocorrerá a escolaha de seus itens
@bot.callback_query_handler(func=lambda call: call.data in produtos_da_categoria)
def escolha_itens(call):
    global lista_produto , dicionario_itens_produto

    mensagem = call.message.message_id
    chat = call.message.chat.id

    dicionario_itens_produto[chat]=list() # aqui eu informo que ele recebera uma lista


    lista=lista_itens(categoria_escolhida[chat], call.data) # cria lista com os itens do produto escolhido
    markup = telebot.types.InlineKeyboardMarkup(row_width=1) # cria o teclado dos itens
    for x in lista: # for de criação do teclado
        botao = telebot.types.InlineKeyboardButton(x, callback_data=x)
        markup.add(botao)
    lista_mensagem=" - ".join(lista)
    bot.send_message(chat, f"Produto escolhido : {call.data}\nPossiveis acompanhamentos: {lista_mensagem} ")
    bot.send_message(chat, "Escolha os Itens que deseja remover do lanche ", reply_markup=markup) # mensagem que trará o teclado

    for x in range(mensagem, mensagem - 5, -1):
        try:
            bot.delete_message(chat, x)
        except:
            pass



 # para isso farei um botão de prosseguir que me levará a a proxima tela , lembrar de colocar a mensagens dos itens escolhidos
    # farei a lógica para criar a lista com todos  os itens , variavel normal
    # depois criarei uma teclado com essas opções
    # esse teclado terá opção de proseguir com o pedido




mensagem_acumulada_itens=int()
@bot.callback_query_handler(func=lambda call: call.data in itens)
def itens_escolha(call):
    global  dicionario_itens_produto, mensagem_acumulada_itens

    mensagem = call.message.message_id
    chat = call.message.chat.id

    if mensagem_acumulada_itens: # deleta a mensagem e insere None no acumulador
        bot.delete_message(chat,mensagem_acumulada_itens)
        mensagem_acumulada_itens=None


    if call.data in dicionario_itens_produto[chat]: # lógica para acrescentar itens
        dicionario_itens_produto[chat].remove(call.data)
    else:
        dicionario_itens_produto[chat].append(call.data)
    lista= " - ".join(dicionario_itens_produto[chat])

    markup= telebot.types.InlineKeyboardMarkup(row_width=1)
    botão=telebot.types.InlineKeyboardButton("Prosseguir",callback_data="pros")
    markup.add(botão)
    mensagem=bot.send_message(chat,f"Itens adicionados : {lista}\n Deseja prosseguir"
                                   f" com o pedido? Caso ainda queira é só retirar mais itens",reply_markup=markup) # dispara a mensagem e atribui  informações da mensagem
    mensagem_acumulada_itens=mensagem.message_id # recebe seu id




bot.polling()