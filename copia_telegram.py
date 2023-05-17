
import telebot
from telebot import types

bot=telebot.TeleBot("6218006765:AAF309hpXCmaU1r9P41zKiNK1L8gaqTMyqI")

##Cria uma receptor que receberá qualquer mensagem digitada e retornará uma mensagem com um botão como padrão.
#Utilizada geralmente para mensagem inicial.
# podendo ser alterada a quantidade de botões adicionando mais.
# Aqui ultima_mensagem já recebendo a id da ultima mensagem

ultima_mensagem_id=None
@bot.message_handler(func=lambda message: True)
def inicio(message):
    global ultima_mensagem_id
    if ultima_mensagem_id == None:
        markup = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton('Texto da mensagem', callback_data='indicador call')
        markup.add(but1)
        mensagem=bot.send_message(message.chat.id, text="Texdo da mensagem", reply_markup=markup) # lembrando que text não pode estar vazio
        ultima_mensagem_id=mensagem.message_id
    else:
        bot.delete_message(message.chat.id, ultima_mensagem_id)
        ultima_mensagem = None

        markup = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton('Texto da mensagem', callback_data='indicador call')
        markup.add(but1)
        mensagem = bot.send_message(message.chat.id, text="Texdo da mensagem",reply_markup=markup)  # lembrando que text não pode estar vazio
        ultima_mensagem_id = mensagem.message_id





#guarda o que foi digiado e permite especificar a próxima função que será executada
# A primeira função é chamada normalmente tanto o seu call quando sua messagem podem ser usados com o valor normal
# até chegar no bot.register_next_step_handler, nesse momento ele ficará a espera do que será digitado para
#enviar para proxima função

@bot.callback_query_handler(func=lambda call: call.data == 'callback do botão')
def iniciar_conversa(call): se for (messagem)
    bot.send_message(message ou call.message.chat.id, "texto da mensagem que pode ser usado para pedir um texto")
    bot.register_next_step_handler(call.message, "nome da função a ser chamada")






# Cria 1 botão com um markup , podendo desse momento em diante fazer ctrl-c ctrl-v dos botões
"markup nome" = telebot.types.InlineKeyboardMarkup()
"botao nome" = telebot.types.InlineKeyboardButton('texto do botão', callback_data='comando dele')
markup.add(botao)







# Atende ao tocar de um botão inline devolvendo uma mensagem de texto podendo ter a indicação para botões.
# Lembrando que aqui dentro já temos a ultima_mensagem para podermos excluir
@bot.callback_query_handler(func=lambda call: call.data == 'callback do botão')
def botao_clicado(call):
 global ultima_mensagem_id

 if ultima_mensagem_id!=None:

    bot.delete_message(call.message.chat.id,ultima_mensagem_id)
    ultima_mensagem_id=None
    bot.answer_callback_query(call.id, text= "texto ao clicar no botão")
    mensagem=bot.send_message(call.message.chat.id, text= "texto na mensagem", reply_markup="markup")
    ultima_mensagem_id=mensagem.message_id
 else:

     bot.answer_callback_query(call.id, text="texto ao clicar no botão")
     mensagem=bot.send_message(call.message.chat.id, text="texto na mensagem", reply_markup="markup")
     ultima_mensagem_id = mensagem.message_id







#Remove um teclado da tela
def vai(message):
    markup = ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "Keyboard has been removed", reply_markup=markup)






# permite criar uma lista de botões embasado em uma lista
produtos = ['Opção 1', 'Opção 2', 'Opção 3', 'Opção 1', 'Opção 2', 'Opção 3']
keyboard = ReplyKeyboardMarkup(row_width=1)
for opcao in produtos:
    keyboard.add(opcao)




bot.polling()