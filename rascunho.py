import telegram # importa a biblioteca telegram
from telegram.ext import Updater, CommandHandler # importa as classes Updater e CommandHandler da sub-biblioteca telegram.ext

bot = telegram.Bot(token="6218006765:AAF309hpXCmaU1r9P41zKiNK1L8gaqTMyqI") # cria uma instância do bot usando o token de acesso
updater = Updater(token="6218006765:AAF309hpXCmaU1r9P41zKiNK1L8gaqTMyqI", use_context=True) # cria uma instância do updater usando o bot e habilitando o uso de contextos
dispatcher = updater.dispatcher # cria uma instância do dispatcher que vai gerenciar os manipuladores de mensagens

def welcome(update, context): # define uma função chamada welcome que recebe dois argumentos: update e context
    update.message.reply_text('Olá, seja bem-vindo ao meu bot!') # envia uma mensagem de texto para o chat que enviou a mensagem original

welcome_handler = CommandHandler('start', welcome) # cria um objeto CommandHandler que vai chamar a função welcome quando receber o comando /start

dispatcher.add_handler(welcome_handler) # adiciona o welcome_handler ao dispatcher

updater.start_polling() # inicia o polling para receber as atualizações do Telegram
