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


bot.polling()