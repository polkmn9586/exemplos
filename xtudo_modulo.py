import telebot
from telebot.types import ReplyKeyboardMarkup,ReplyKeyboardRemove
def apaga_mensagem_usuario(bot,message):

    bot.delete_message(message.chat.id, message.message_id)
def apaga_mensagem_usuario_call(bot, call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

def apaga_mensagem_bot(bot,message):
    global ultima_mensagem_id

    bot.delete_message(message.chat.id, ultima_mensagem_id)  # Deletando id da ultima mensagem
    ultima_mensagem_id = None


def apaga_mensagem_bot_call(bot,call):
    global ultima_mensagem_id

    bot.delete_message(call.message.chat.id, ultima_mensagem_id)  # Deletando id da ultima mensagem
    ultima_mensagem_id = None

def mensagem_botao_salva(bot,message,texto,teclado=None):
    """Cria uma mensagem com teclado, caso o queira e salva o id da última mensagem """
    global ultima_mensagem_id

    mensagem = bot.send_message(message.chat.id, text=texto, reply_markup=teclado)
    ultima_mensagem_id = mensagem.message_id


def mensagem_botao_salva_call(bot, call, texto,teclado=None):
    """Cria uma mensagem com teclado, caso o queira e salva o id da última mensagem , isso em call"""
    global ultima_mensagem_id

    mensagem=bot.send_message(call.message.chat.id,text=texto,reply_markup=teclado)
    ultima_mensagem_id=mensagem.message_id

def apaga_janela_selecao(bot,message):
 """ Apagara a janela de seleção, incluirá valor da id da mensagem e retornará uma mensagem"""
 global ultima_mensagem_id
 markup = ReplyKeyboardRemove(selective=False)
 mensagem=bot.send_message(message.chat.id, "Digite o novo valor desejado:", reply_markup=markup)
 ultima_mensagem_id = mensagem.message_id

def adic_categoria(message):
    global dados
    dados[message] = None