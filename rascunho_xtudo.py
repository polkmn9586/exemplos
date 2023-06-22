
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


categoria={}

#---------------------------criar funções com as categorias produtos e itens--------------------------------

def lista_categorias():
    categorias=loja_data.keys()
    return categorias
def lista_produtos(categoria):
    produtos=loja_data.get(categoria, {})
    return produtos.keys()

def lista_itens(categoria,produto):
    itens=loja_data[categoria][produto].get("Itens",[])
    return itens

#---------------------------Fim da criação das funções com as categorias produtos e itens--------------------------------

#---------------------------mensagem inicial -------------------------------------------------------------------------
@bot.message_handler(func=lambda message: True)
def inicio(message):
    mensagem= message.message_id
    chat=message.chat.id
    for x in range(mensagem,mensagem-5,-1):
       try:
        bot.delete_message(chat,x)
       except:
           pass
    markup= telebot.types.InlineKeyboardMarkup(row_width=1)
    botao=telebot.types.InlineKeyboardButton("Fazer um pedido",callback_data="pedido")
    markup.add(botao)
    bot.send_message(message.chat.id, " Seja bem vindo a nossa loja",reply_markup=markup)


#-------------------------------Escolha da categoria em que está o produto-----------------------------------------------
categorias=lista_categorias()
@bot.callback_query_handler(func= lambda call: call.data == "pedido")
def escolha_categoria(call):

    mensagem = call.message.message_id
    chat = call.message.chat.id
    for x in range(mensagem, mensagem - 5, -1):
        try:
            bot.delete_message(chat, x)
        except:
            pass


    markup=telebot.types.InlineKeyboardMarkup(row_width=1)
    for x in categorias:
     botao=telebot.types.InlineKeyboardButton(x,callback_data=x)
     markup.add(botao)
    bot.send_message(chat,"Escolha a categoria do produto", reply_markup=markup )


@bot.callback_query_handler(func= lambda call: call.data in categorias)
def escolha_produtos(call):
    mensagem = call.message.message_id
    chat = call.message.chat.id
    produtos=lista_produtos(call.data)

    for x in range(mensagem, mensagem - 5, -1):
        try:
            bot.delete_message(chat, x)
        except:
            pass
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    for x in produtos:
        botao = telebot.types.InlineKeyboardButton(x, callback_data=x)
        markup.add(botao)
    bot.send_message(chat, "Escolha a categoria do produto", reply_markup=markup)

bot.polling()