import telebot

def apaga_mensagem_usuario(bot,message):

    bot.delete_message(message.chat.id, message.message_id)

def apaga_mensagem_bot(bot,message,ultima):

    bot.delete_message(message.chat.id, ultima)  # Deletando id da ultima mensagem
    ultima_mensagem_id = None

def salva_id_ultima_mensagem(bot,message,):
    global ultima_mensagem_id
    mensagem = bot.send_message(message.chat.id, text="Configuração:", parse_mode="HTML", reply_markup=markup)
    ultima_mensagem_id = mensagem.message_id

