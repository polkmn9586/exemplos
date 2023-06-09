import telebot
from telebot.types import ReplyKeyboardMarkup,ReplyKeyboardRemove

def apaga_mensagem_usuario(bot,message):

    bot.delete_message(message.chat.id, message.message_id)
def apaga_mensagem_usuario_call(bot, call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
def apaga_mensagem_bot(bot,message):
    global ultima_mensagem_id

    bot.delete_message(message.chat.id, ultima_mensagem_id)  # Deletando id da ultima mensagem
def apaga_mensagem_bot_call(bot,call):

    bot.delete_message(call.message.chat.id, ultima_mensagem_id)  # Deletando id da ultima mensagem





def apaga_janela_selecao(bot,message,texto):
 """ Apagara a janela de seleção, incluirá valor da id da mensagem e retornará uma mensagem"""
 markup = ReplyKeyboardRemove(selective=False)
 mensagem=bot.send_message(message.chat.id, texto, reply_markup=markup)
 return mensagem.message_id
def delete_all_messages(bot):

    updates = bot.get_updates()
    print(updates)
def apaga_mensagem(bot,message):
    message_id=message.message_id
    bot.delete_message(message.chat.id, message_id)  # Deletando id da ultima mensagem
def apaga_mensagem_call(bot,call):
    """Apaga a mensagem que está sendo recebida pelo call"""
    message_id = call.message.message_id
    bot.delete_message(call.message.chat.id, message_id)  # Deletando id da ultima mensagem
def apaga_mensagem_id(bot,message,message_id):
    """Permite apagar mensagem coso se tenha a id da mesma . E ele precisa retornar None para que a não cause
       erro tentando apagar uma mensagem 2 x"""

    bot.delete_message(message.chat.id, message_id)  # Deletando id da ultima mensagem
    return None
def apaga_mensagem_id_call(bot,call,message_id):
    """Permite apagar mensagem coso se tenha a id da mesma"""
    bot.delete_message(call.message.chat.id, message_id)  # Deletando id da ultima mensagem
    return None



def mensagem_botao_salva(bot,message,texto,teclado=None):
    """Cria uma mensagem com teclado, caso o queira e salva o id da última mensagem """
    mensagem = bot.send_message(message.chat.id, text=texto, reply_markup=teclado)
    return mensagem.message_id
def mensagem_botao_salva_call(bot, call, texto,teclado=None):
    """Cria uma mensagem com teclado, caso o queira e salva o id da última mensagem , isso em call"""
    mensagem=bot.send_message(call.message.chat.id,text=texto,reply_markup=teclado)
    return mensagem.message_id
def mensagem_botao_salva_1botao(bot,message,texto,texto_botão,comando):

    markup = telebot.types.InlineKeyboardMarkup()
    botao1 = telebot.types.InlineKeyboardButton(texto_botão, callback_data=comando)
    markup.add(botao1)

    mensagem = bot.send_message(message.chat.id, text=texto, reply_markup=markup)

    return mensagem.message_id
def mensagem_botao_salva_2botoes(bot,message,texto_mesagem,texto1,texto2,comando1,comando2):

    markup = telebot.types.InlineKeyboardMarkup()
    botao1 = telebot.types.InlineKeyboardButton(texto1, callback_data=comando1)
    botao2 = telebot.types.InlineKeyboardButton(texto2, callback_data=comando2)
    markup.add(botao1,botao2)

    mensagem = bot.send_message(message.chat.id, text=texto_mesagem, reply_markup=markup)

    return mensagem.message_id
def mensagem_botao_salva_call_2botoes(bot,call,texto_mesagem,texto1,texto2,comando1,comando2):

    markup = telebot.types.InlineKeyboardMarkup()
    botao1 = telebot.types.InlineKeyboardButton(texto1, callback_data=comando1)
    botao2 = telebot.types.InlineKeyboardButton(texto2, callback_data=comando2)
    markup.add(botao1,botao2)

    mensagem = bot.send_message(call.message.chat.id, text=texto_mesagem, reply_markup=markup)

    return mensagem.message_id
def mensagem_botao_salva_call_3botoes(bot,call,texto_mesagem,texto1,texto2,texto3,comando1,comando2,comando3):

    markup = telebot.types.InlineKeyboardMarkup()
    botao1 = telebot.types.InlineKeyboardButton(texto1, callback_data=comando1)
    botao2 = telebot.types.InlineKeyboardButton(texto2, callback_data=comando2)
    botao3 = telebot.types.InlineKeyboardButton(texto3, callback_data=comando3)
    markup.add(botao1,botao2,botao3)

    mensagem = bot.send_message(call.message.chat.id, text=texto_mesagem, reply_markup=markup)

    return mensagem.message_id
def mensagem_botao_salva_1botao_call(bot,call,texto,texto_bot,comando_bot):

    markup = telebot.types.InlineKeyboardMarkup()
    botao1 = telebot.types.InlineKeyboardButton(texto_bot, callback_data=comando_bot)
    markup.add(botao1)

    mensagem = bot.send_message(call.message.chat.id, text=texto, reply_markup=markup)

    return mensagem.message_id


def cria_caixa_selecao(lista):
    """ Será criada uma caixa de seleção com os nomes de uma lista ou dicionário , sendo no caso do dcionário usados o keys"""
    lista = [x for x in lista]  # criação da lista  de categoria

    keyboard = ReplyKeyboardMarkup(
        row_width=1)  # utilizando a lista para criar com os seus itens uma caixa de seleção
    if lista=={}:
        return None
    else:

      for opcao in lista:
        keyboard.add(opcao)

      return keyboard


def cria_caixa_selecao_com_1opcao(lista,opcao1):
    """ Será criada uma caixa de seleção com os nomes de uma lista ou dicionário , sendo no caso do dcionário usados o keys"""
    lista = [x for x in lista]  # criação da lista  de categoria

    keyboard = ReplyKeyboardMarkup(
        row_width=1)  # utilizando a lista para criar com os seus itens uma caixa de seleção
    if lista == {}:
        return None
    else:

        for opcao in lista:
            keyboard.add(opcao)
        keyboard.add(opcao1)
        return keyboard
def cria_caixa_selecao_com_2opcao(lista,opcao1,opcao2):
    """ Será criada uma caixa de seleção com os nomes de uma lista ou dicionário , sendo no caso do dcionário usados o keys"""
    lista = [x for x in lista]  # criação da lista  de categoria

    keyboard = ReplyKeyboardMarkup(
        row_width=1)  # utilizando a lista para criar com os seus itens uma caixa de seleção
    if lista == {}:
        return None
    else:

        for opcao in lista:
            keyboard.add(opcao)
        keyboard.add(opcao1)
        keyboard.add(opcao2)
        return keyboard


def adic_categoria(message):
    global dados
    dados[message] = None