import telebot
from telebot import types


pedido = []

# Cria o bot e obtém o token do BotFather
bot = telebot.TeleBot("6218006765:AAF309hpXCmaU1r9P41zKiNK1L8gaqTMyqI")

# Cria o botão de entrada
btn = types.InlineKeyboardButton(text='🥪 Vamos iniciar nosso pedido 🌭', callback_data='inicio',
                                 description='Alguma descrição')
inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
inline_keyboard.add(btn)

# cria o botão de inicio do pedido
inline_keyboard1 = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton(text='🥪 Cachorro quente 🌭', callback_data='cachorro',
                                  description='Alguma descrição')
btn2 = types.InlineKeyboardButton(text='🥪 X-tudo 🌭', callback_data='x-tudo', description='Alguma descrição')
inline_keyboard1.add(btn1, btn2)

# mensagem inicial com o botão de entrada
inicio = bot.send_message(chat_id=1594098043, text="🌭 Vamos de que hoje?🌭\n 🌭Já estamos atendendo🌭 ",
                          reply_markup=inline_keyboard)

# Função que será executada quando o botão de entrada for clicado
@bot.callback_query_handler(func=lambda call: call.data == 'inicio')
def on_callback_query(call):
    with open("C:/Users/merca/OneDrive/Área de Trabalho/download.jpeg", 'rb') as photo:
        bot.send_photo(chat_id=1594098043, reply_markup=inline_keyboard1, photo=photo)

# Envia a mensagem inicial com o teclado inline

# Inicia o bot
bot.polling()










