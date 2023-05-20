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
    global ultima_mensagem_id
    bot.delete_message(call.message.chat.id, ultima_mensagem_id)  # Deletando id da ultima mensagem





def apaga_janela_selecao(bot,message,texto):
 """ Apagara a janela de seleção, incluirá valor da id da mensagem e retornará uma mensagem"""
 global ultima_mensagem_id
 markup = ReplyKeyboardRemove(selective=False)
 mensagem=bot.send_message(message.chat.id, texto, reply_markup=markup)
 return mensagem.message_id
def delete_all_messages(bot):

    updates = bot.get_updates()
    print(updates)
    """for update in updates:
        message = update.message
        chat_id = message.chat.id
        message_id = message.message_id
        print(update.message)
        bot.delete_message(chat_id, message_id)

    delete_all_messages()
"""
def apaga_mensagem(bot,message):
    global ultima_mensagem_id
    ultima_mensagem_id = message.message_id
    if ultima_mensagem_id != None:
        bot.delete_message(message.chat.id, ultima_mensagem_id)  # Deletando id da ultima mensagem
def apaga_mensagem_call(bot,call):
    global ultima_mensagem_id
    ultima_mensagem_id = call.message.message_id
    if ultima_mensagem_id != None:
        bot.delete_message(call.message.chat.id, ultima_mensagem_id)  # Deletando id da ultima mensagem



def mensagem_botao_salva(bot,message,texto,teclado=None):
    """Cria uma mensagem com teclado, caso o queira e salva o id da última mensagem """
    global ultima_mensagem_id

    mensagem = bot.send_message(message.chat.id, text=texto, reply_markup=teclado)
    ultima_mensagem_id = mensagem.message_id
    return mensagem.message_id
def mensagem_botao_salva_call(bot, call, texto,teclado=None):
    """Cria uma mensagem com teclado, caso o queira e salva o id da última mensagem , isso em call"""
    global ultima_mensagem_id

    mensagem=bot.send_message(call.message.chat.id,text=texto,reply_markup=teclado)
    ultima_mensagem_id=mensagem.message_id
    return mensagem.message_id
def mensagem_botao_salva_1botao(bot,message,texto):
    global ultima_mensagem_id
    markup = telebot.types.InlineKeyboardMarkup()
    botao1 = telebot.types.InlineKeyboardButton('texto do botão', callback_data='comando dele')
    markup.add(botao1)

    mensagem = bot.send_message(message.chat.id, text=texto, reply_markup=markup)

    return mensagem.message_id
def mensagem_botao_salva_1botao_call(bot,call,texto):
    global ultima_mensagem_id
    markup = telebot.types.InlineKeyboardMarkup()
    botao1 = telebot.types.InlineKeyboardButton('texto do botão', callback_data='comando dele')
    markup.add(botao1)

    mensagem = bot.send_message(call.message.chat.id, text=texto, reply_markup=markup)

    return mensagem.message_id








def adic_categoria(message):
    global dados
    dados[message] = None