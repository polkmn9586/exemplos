import json

import telebot
from telebot import TeleBot
from telebot import types
from telebot.types import ReplyKeyboardMarkup,ReplyKeyboardRemove

from xtudo_modulo import apaga_mensagem_usuario, apaga_mensagem_bot , mensagem_botao_salva, \
                         apaga_mensagem_usuario_call,mensagem_botao_salva_call,\
                         apaga_mensagem_bot_call,apaga_janela_selecao,mensagem_botao_salva_1botao,\
                         mensagem_botao_salva_1botao_call,delete_all_messages,apaga_mensagem,apaga_mensagem_call, \
                         cria_caixa_selecao,apaga_mensagem_ultima,mensagem_botao_salva_2botoes,mensagem_botao_salva_call_2botoes,\
                         mensagem_botao_salva_call_3botoes,apaga_mensagem_call_ultima

from funcao_com_json import lendo_arquivo_json_dic,escrevendo_json_novo

bot=telebot.TeleBot("6218006765:AAF309hpXCmaU1r9P41zKiNK1L8gaqTMyqI")



produtos_preco={}
produto_troca=""


ultima_mensagem_id=None
categoria=""  # servira para armazenar a categoria  de algumas funções
produto=""
valor=""
itens=""
message_ids=[]
categoria_excluida=""
categoria_exclui_produto="" # Usado para armazenar a categoria da onde se encontra o produto ou o item a ser excluido
produto_excluido=""#produto da exclusão
item_excluido=""
categoria_exclui_item="" # Usado para armazenar o produto a onde se encontra o item a ser excluido
produto_exclui_item="" # item da exclusão
dados=lendo_arquivo_json_dic("loja.json") # Leitura do arquivo json carregando a variável dados





# ------------------------Define um manipulador de mensagem para o comando /limpar--------------------------

acumulador="" # receberá a message da função a seguir
@bot.callback_query_handler(func=lambda call: call.data=="limpar")
def limpar_tela(call):
    global ultima_mensagem_id
    ultima_mensagem_id=call.message.message_id
    # Obtém o ID do chat da mensagem
    chat_id = call.message.chat.id

    # Obtém a ID da mensagem
    message_id = call.message.message_id

    # Percorre as mensagens anteriores da mesma conversa
    for i in range(message_id - 1, message_id-10 , -1):
        print(i)
        # Tenta apagar a mensagem com a ID i
        try:
            bot.delete_message(chat_id, i)
        # Se ocorrer um erro, significa que a mensagem não existe ou não pode ser apagada
        except:
            # Ignora o erro e continua o loop
            pass


#-----------------------------Imprimindo o catalogo---------------------------------------------------------


@bot.callback_query_handler(func=lambda call: call.data=='mensagem')
def enviar_mensagem(call):
    global ultima_mensagem_id, texto
    texto = ""
    for categoria, produtos in dados.items():
        texto += f"- Categoria: {categoria}\n\n"
        for produto, info in produtos.items():
            texto += f"  Produto: {produto}\n"
            texto += f"  Valor: {info['Valor']}\n"
            texto += f"  Itens: {', '.join(info['Itens'])}\n\n"
    if ultima_mensagem_id!=None:

     bot.delete_message(call.message.chat.id, ultima_mensagem_id)

    ultima_mensagem_id=mensagem_botao_salva_1botao_call(bot,call,texto,"Menu iniciar","inicio")







#Mensagem inicial ao escrever algo na tela
@bot.message_handler(func=lambda message: True)
def inicio(message):

      global ultima_mensagem_id


      markup = types.InlineKeyboardMarkup()  # Criação do teclado menu inicial
      but2 = types.InlineKeyboardButton('Criar categoria ou produto', callback_data='criar')
      but4 = types.InlineKeyboardButton('excluir: categoria , produto ou item', callback_data='excluir')
      but1 = types.InlineKeyboardButton('Imprimir catálogo', callback_data='mensagem')
      but3 = types.InlineKeyboardButton('Limpar a tela', callback_data='limpar')
      markup.add(but3)
      markup.add(but2)
      markup.add(but4)  # Incorporando os botões
      markup.add(but1)
      ultima_mensagem_id=mensagem_botao_salva(bot, message, "--------------------Configuração--------------------",markup)  # Mensagem com o teclado e a atualização da id da
      apaga_mensagem(bot, message)

          # ultima mensagem


#--------------iniciar a exclusão de uma categoria / produto / item------------------------------------------------------


# Aqui a escolha do que será excluido
@bot.callback_query_handler(func=lambda call: call.data == 'excluir')
def exclusao(call):
    global ultima_mensagem_id
    mensagem_botao_salva_call_3botoes(bot,call,"O que deseja excluir?","Categoria","Produtos","Itens","excluir_categorias","excluir_produtos","excluir_itens")
    apaga_mensagem_call(bot, call)


                 # ---------------------inicio da exclusão da categoria------------------------------

#Aqui ocorre a escolha da categoria que será excluida
@bot.callback_query_handler(func=lambda call: call.data == 'excluir_categorias')
def exclusao(call):
 global ultima_mensagem_id

 keyboard=cria_caixa_selecao(dados)
 if dados == {} or None:

    ultima_mensagem_id=mensagem_botao_salva_1botao_call(bot,call,"Você não possui nenhuma categoria cadastrada","Menu inicial","inicio")
    apaga_mensagem_call(bot, call)

 else:
     ultima_mensagem_id = mensagem_botao_salva_call(bot, call, "Escolha a categoria que será excluida",keyboard)
     apaga_mensagem_call(bot, call)
     bot.register_next_step_handler(call.message, excluir_categoria)

# Pedido de confirmação da exclusão da categoria
def excluir_categoria(message):

    global ultima_mensagem_id,categoria_excluida


    categoria_excluida=message.text #Recebe o que será excluído

    #apaga_mensagem_ultima(bot, message)
    #apaga_mensagem(bot, message)
    bot.delete_message(message.chat.id,ultima_mensagem_id)


    ultima_mensagem_id =mensagem_botao_salva_2botoes(bot,message,f"Voce confirma a exclusão de: {message.text} ","Sim","Não","sim_excluir_categoria","inicio")
    apaga_mensagem(bot, message)

#Aqui ocorre de fato a exclusão
@bot.callback_query_handler(func=lambda call: call.data == 'sim_excluir_categoria')
def exclusao(call):
    global categoria_excluida
    del dados[categoria_excluida]
    escrevendo_json_novo(dados,"loja.json")
    mensagem_botao_salva_call_2botoes(bot,call,"Excluida com sucesso","Excluir outra","Menu inicial","excluir","inicio")
    apaga_mensagem_call(bot,call)

       # ---------------------Fim da exclusão da categoria------------------------------




       # -------------------inicio da exclusão do produto------------------------------




#Aqui será escolhida a categoria da exclusão do produto
@bot.callback_query_handler(func=lambda call: call.data == 'excluir_produtos')
def exclusao(call):
 global ultima_mensagem_id,dados

 keyboard=cria_caixa_selecao(dados)

 if dados == {} or None:

    ultima_mensagem_id=mensagem_botao_salva_1botao_call(bot,call,"Você não possui nenhuma categoria cadastrada","Menu inicial","inicio")
    apaga_mensagem_call(bot, call)

 else:
     keyboard = cria_caixa_selecao(dados)
     ultima_mensagem_id = mensagem_botao_salva_call(bot, call, "Escolha a categoria em que se encontra o produto",keyboard)
     apaga_mensagem_call(bot, call)
     bot.register_next_step_handler(call.message, excluir_produtos1)

# Aqui será criada a lista de produtos e a escolha daquele que será excluido
def excluir_produtos1(message):
 global ultima_mensagem_id,categoria_exclui_produto
 bot.delete_message(message.chat.id, ultima_mensagem_id)

 categoria_exclui_produto=message.text # Recebendo a categoria aonde se encontra o produto
 apaga_mensagem(bot, message)


 if dados[message.text]== {} or None:

    ultima_mensagem_id=mensagem_botao_salva_1botao(bot,message,"Você não possui nenhum produto cadastrado","Menu inicial","inicio")


 else:
     keyboard = cria_caixa_selecao(dados[message.text])

     ultima_mensagem_id = mensagem_botao_salva(bot, message, "Escolha o produto que será excluido",keyboard)

     bot.register_next_step_handler(message, excluir_pergunta_produto)

#Pedido de confirmação para exclusão do produto
def excluir_pergunta_produto(message):
    global ultima_mensagem_id, produto_excluido

    produto_excluido=message.text

    bot.delete_message(message.chat.id, ultima_mensagem_id)

    ultima_mensagem_id = mensagem_botao_salva_2botoes(bot, message, f"Voce confirma a exclusão de: {message.text} ",
                                                      "Sim", "Não", "sim_excluir_produto", "inicio")
    apaga_mensagem(bot, message)

#Aqui ocorre de fato a exclusão do produto
@bot.callback_query_handler(func=lambda call: call.data == 'sim_excluir_produto')
def exclusao(call):
    global categoria_exclui_produto,produto_excluido,dados
    del dados[categoria_exclui_produto][produto_excluido]
    escrevendo_json_novo(dados,"loja.json")
    mensagem_botao_salva_call_2botoes(bot,call,"Excluida com sucesso","Excluir outra","Menu inicial","excluir","inicio")
    apaga_mensagem_call(bot,call)






#Aqui será escolhida a categoria da exclusão do item
@bot.callback_query_handler(func=lambda call: call.data == 'excluir_itens')
def exclusao(call):
 global ultima_mensagem_id,dados



 if dados == {} or None:

    ultima_mensagem_id=mensagem_botao_salva_1botao_call(bot,call,"Você não possui nenhuma categoria cadastrada","Menu inicial","inicio")
    apaga_mensagem_call(bot, call)

 else:
     keyboard = cria_caixa_selecao(dados)
     ultima_mensagem_id = mensagem_botao_salva_call(bot, call, "Escolha a categoria em que se encontra o item",keyboard)
     apaga_mensagem_call(bot, call)
     bot.register_next_step_handler(call.message, categoria_iten)


#Aqui será armazenada a categoria e escolhido o produto da exclusão do item
def categoria_iten(message):
 global ultima_mensagem_id,dados,categoria_exclui_item

 categoria_exclui_item=message.text


 if dados[categoria_exclui_item] == {} or None:

    ultima_mensagem_id=mensagem_botao_salva_1botao(bot,message,"Esse seu produto está sem itens, logo não ha nada para excluir"
                                                               " ","Menu inicial","inicio")
    apaga_mensagem(bot, message)

 else:
     keyboard = cria_caixa_selecao(dados[categoria_exclui_item])
     apaga_mensagem(bot, message)
     ultima_mensagem_id = mensagem_botao_salva(bot, message, "Escolha o produto em que se encontra o item",keyboard)


     bot.register_next_step_handler(message, produtos_iten)

#Aqui será armazenado o produto e escolhido o item
def produtos_iten(message):

    global ultima_mensagem_id,dados,categoria_exclui_item,produto_exclui_item
    produto_exclui_item=message.text

    if dados[categoria_exclui_item][message.text]["Itens"] == [] or None:

        ultima_mensagem_id = mensagem_botao_salva_1botao(bot, message, "Você não possui nenhuma categoria cadastrada",
                                                         "Menu inicial", "inicio")
        apaga_mensagem(bot, message)

    else:
        keyboard = cria_caixa_selecao(dados[categoria_exclui_item][produto_exclui_item]["Itens"])
        ultima_mensagem_id = mensagem_botao_salva(bot, message, "Escolha o item a ser excluido", keyboard)
        apaga_mensagem(bot, message)
        bot.register_next_step_handler(message, excluir_pergunta_item)


#Aqui a pergunta sobre a exclusão do item
def excluir_pergunta_item(message):
    global ultima_mensagem_id, item_excluido
    item_excluido=message.text


    bot.delete_message(message.chat.id, ultima_mensagem_id)

    ultima_mensagem_id = mensagem_botao_salva_2botoes(bot, message, f"Voce confirma a exclusão de: {message.text} ",
                                                      "Sim", "Não", "sim_excluir_item", "inicio")
    apaga_mensagem(bot, message)




#Aqui ocorre de fato a exclusão do item
@bot.callback_query_handler(func=lambda call: call.data == 'sim_excluir_item')
def exclusao(call):

    global ultima_mensagem_id,categoria_exclui_produto,produto_exclui_item,dados,item_excluido
    recebe=dados[categoria_exclui_item][produto_exclui_item]["Itens"]

    recebe.remove(item_excluido)
    dados[categoria_exclui_item][produto_exclui_item]["Itens"]=recebe

    escrevendo_json_novo(dados,"loja.json")
    mensagem_botao_salva_call_2botoes(bot,call,"Excluido com sucesso","Excluir outro","Menu inicial","excluir","inicio")
    apaga_mensagem_call(bot,call)




#--------------iniciar a criação de uma categoria / produto------------------------------------------------------

# pergunta o que quer criar, produto ou categoria
@bot.callback_query_handler(func=lambda call: call.data == 'criar')
def botao_clicado4(call):


     global ultima_mensagem_id


     markup = telebot.types.InlineKeyboardMarkup()
     bot1= types.InlineKeyboardButton('Categoria', callback_data='cria_categoria')
     bot2 = types.InlineKeyboardButton('Produto', callback_data='cria_produto')
     bot3 =types.InlineKeyboardButton('Retornar', callback_data='inicio')
     markup.add(bot1,bot2,bot3)
     ultima_mensagem_id=mensagem_botao_salva_call(bot,call,"Escolha categoria ou produto",markup)
     apaga_mensagem_call(bot, call)  # Apaga a mensagem da tela

# Aqui é o momento aonde digitamos o nome da categoria
@bot.callback_query_handler(func=lambda call: call.data == 'cria_categoria')
def botao_clicado1(call):

         global ultima_mensagem_id

         ultima_mensagem_id=mensagem_botao_salva_call(bot,call,"Digite o nome da categoria que deseja criar")
         apaga_mensagem_call(bot, call)
         bot.register_next_step_handler(call.message, adic_categoria) # Avança para uma função determinada independente
                                                                      # da escrita

#Função que cria a categoria
def adic_categoria(message):

    global ultima_mensagem_id,dados

    bot.delete_message(message.chat.id,ultima_mensagem_id)

    if dados == {} or None:
        dados={message.text:{}}
    else:
     dados[message.text] = {} # Aqui eu crio em dados um key com o nome da minha categoria com None

    escrevendo_json_novo(dados,"loja.json")
    print("oi")
    markup  = types.InlineKeyboardMarkup()
    botao1 = types.InlineKeyboardButton('continuar criando', callback_data='cria_categoria')
    botao2 = types.InlineKeyboardButton('retornar ao início', callback_data='inicio')
    markup.add(botao1,botao2)
    ultima_mensagem_id=mensagem_botao_salva(bot,message,f"Categoria criada com sucesso: {message.text}",markup)
    apaga_mensagem(bot, message)



#Essa função será chamada no momento em que se tenta criar um produto ou um produto sem uma categoria
@bot.callback_query_handler(func=lambda call: call.data == 'cria_produto')
def botao_clicado3(call):
        global ultima_mensagem_id

        if dados == {} or None: # Caso do loja.json vazio

            markup = telebot.types.InlineKeyboardMarkup()
            botao1 = telebot.types.InlineKeyboardButton('Retorne', callback_data='inicio')
            markup.add(botao1)
            mensagem_botao_salva_call(bot, call, "Você ainda não possui uma categoria cadastrada , "
                                                 "precisa cadastrar uma para adicionar um produto nela", markup)
        else:


            lista = [x for x in dados]  # criação da lista  de categoria
            keyboard = ReplyKeyboardMarkup(
                row_width=1)  # utilizando a lista para criar com os seus itens uma caixa de seleção

            for opcao in lista:
                keyboard.add(opcao)


            ultima_mensagem_id=mensagem_botao_salva_call(bot, call, "Escolha a categoria que deseja incluir seu produto", keyboard)
            bot.register_next_step_handler(call.message, cria_produto_escoha_categoria)
        apaga_mensagem_call(bot, call)

#Aqui será digitado o nome do produto
def cria_produto_escoha_categoria(message):

    global ultima_mensagem_id, categoria


    categoria = message.text # armazenando valor em categoria para ser usado na proxima função
    bot.delete_message(message.chat.id, ultima_mensagem_id)
    ultima_mensagem_id = apaga_janela_selecao(bot, message, "Digite o nome do produto")
    apaga_mensagem(bot, message)

    bot.register_next_step_handler(message, digite_produto)

def digite_produto(message):

    global ultima_mensagem_id, produto


    produto = message.text # armazenando valor em categoria para ser usado na proxima função

    #apaga_janela_selecao(bot,"Digite o valor do produto")
    bot.delete_message(message.chat.id, ultima_mensagem_id)
    ultima_mensagem_id=mensagem_botao_salva(bot, message, "Digite o valor do produto")
    apaga_mensagem(bot, message)
    bot.register_next_step_handler(message, digite_valor)

def digite_valor(message):

    global ultima_mensagem_id, valor
    valor = message.text # armazenando valor em categoria para ser usado na proxima função


    #apaga_janela_selecao(bot,"Digite os itens do produto")
    bot.delete_message(message.chat.id, ultima_mensagem_id)
    ultima_mensagem_id=mensagem_botao_salva(bot, message, "Digite os itens do produto")
    apaga_mensagem(bot, message)
    bot.register_next_step_handler(message, digite_itens)

def digite_itens(message):

    global ultima_mensagem_id, itens,dados



    itens = message.text # armazenando valor em itens para ser usado
    itens=itens.split()


    markup = telebot.types.InlineKeyboardMarkup()
    botao1 = telebot.types.InlineKeyboardButton('Continuar', callback_data='cria_produto')
    botao2 = telebot.types.InlineKeyboardButton('Menu inicial', callback_data='inicio')
    markup.add(botao1,botao2)

    if dados[categoria]==None: # se for None ele precisa indicar que o proximo elemento é um dic, depois dessa
                               # indicação os demais serão reconhecidos como dic

     dados[categoria]={produto:{"Valor":valor,"Itens":itens}} # Forma para reconhecer como dic

     escrevendo_json_novo(dados,"loja.json")
    else:
     dados[categoria][produto]= {"Valor": valor, "Itens": itens} # Aqui já reconhecido como dic

     escrevendo_json_novo(dados, "loja.json")

    bot.delete_message(message.chat.id, ultima_mensagem_id)
    mensagem_botao_salva(bot, message, f"Cadastro:"
                                       f"\nCategoria: {categoria}"
                                       f"\nProduto: {produto}"
                                       f"\nValor: {valor}"
                                       f"\nItens: {itens}"
                                       f"\nPara continuar cadastrando produto clique em continuar",markup)

    apaga_mensagem(bot, message)


#----------------------------------fim-------------------------------------------------------------------------




# Chamada pelo final da mudança do valor do produto
@bot.callback_query_handler(func=lambda call: call.data=="inicio")
def inicio(call):

  global ultima_mensagem_id

  if ultima_mensagem_id==None:

    markup = types.InlineKeyboardMarkup() #Criação do teclado menu inicial
    but2 = types.InlineKeyboardButton('Criar categoria ou produto ', callback_data='criar')
    but4 = types.InlineKeyboardButton('excluir: categoria, produto ou item', callback_data='excluir')
    but1 = types.InlineKeyboardButton('Imprimir catálogo', callback_data='mensagem')
    but3 = types.InlineKeyboardButton('Limpar a tela', callback_data='limpar')
    markup.add(but2)
    markup.add(but4)
    markup.add(but1)
    markup.add(but3)
    mensagem_botao_salva_call(bot,call,"--------------------Configuração--------------------",markup)

  else:
        # Apaga a mensagem que chamou a função

        markup = types.InlineKeyboardMarkup()  # Criação do teclado menu inicial
        but2 = types.InlineKeyboardButton('Criar categoria ou produto ', callback_data='criar')
        but4 = types.InlineKeyboardButton('excluir: categoria, produto ou item', callback_data='excluir')
        but1 = types.InlineKeyboardButton('Imprimir catálogo', callback_data='mensagem')
        but3 = types.InlineKeyboardButton('Limpar a tela', callback_data='limpar')
        markup.add(but2)
        markup.add(but4)
        markup.add(but1)
        markup.add(but3)
        ultima_mensagem_id=mensagem_botao_salva_call(bot,call,"--------------------Configuração--------------------",markup)
        apaga_mensagem_call(bot, call)


# Entra na tela alterar produto ou item
@bot.callback_query_handler(func=lambda call: call.data == 'alterar')
def botao_clicado(call):
  global ultima_mensagem_id

  if ultima_mensagem_id !=None:

    ultima_mensagem_id=None
    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Produto', callback_data='produto')
    but2 = types.InlineKeyboardButton('Item', callback_data='item')
    but3 = types.InlineKeyboardButton('Voltar', callback_data='voltar')

    markup.add(but1)
    markup.add(but2)
    markup.add(but3)

    mensagem=bot.send_message(call.message.chat.id, text="Modificação", reply_markup=markup)
    ultima_mensagem_id=mensagem.message_id
  else:
      markup = types.InlineKeyboardMarkup()
      but1 = types.InlineKeyboardButton('Produto', callback_data='produto')
      but2 = types.InlineKeyboardButton('Item', callback_data='item')
      but3 = types.InlineKeyboardButton('Voltar', callback_data='voltar')
      bot.answer_callback_query(call.id, text="texto ao clicar no botão")

      markup.add(but1)
      markup.add(but2)
      markup.add(but3)

      mensagem=bot.send_message(call.message.chat.id, text="Modificação", reply_markup=markup)
      ultima_mensagem_id = mensagem.message_id


@bot.callback_query_handler(func=lambda call: call.data == 'produto')
def botao_clicado(call):
 global ultima_mensagem_id

 if ultima_mensagem_id!=None:
    global produto


    ultima_mensagem_id = None
    keyboard = ReplyKeyboardMarkup(row_width=1)
    for opcao in produtos_preco.keys():
         keyboard.add(opcao)

    mensagem=bot.send_message(call.message.chat.id, 'Escolha uma opção:', reply_markup=keyboard)
    ultima_mensagem_id=mensagem.message_id
    bot.register_next_step_handler(call.message, produto_troca_valor)

 else:

     keyboard = ReplyKeyboardMarkup(row_width=1)
     for opcao in produtos_preco.keys():
         keyboard.add(opcao)
     mensagem_botao_salva_call(bot, call, keyboard, 'Escolha uma opção:')



def produto_troca_valor(message):

 global produto_troca
 global ultima_mensagem_id


 ultima_mensagem_id = None

 produto_troca=message.text
 markup = ReplyKeyboardRemove(selective=False)
 mensagem=bot.send_message(message.chat.id, "Digite o novo valor desejado:", reply_markup=markup)
 ultima_mensagem_id=mensagem.message_id
 bot.register_next_step_handler(message,produto_valor_final)


def produto_valor_final(message):
    global produto_troca
    global ultima_mensagem_id

  
    produtos_preco[produto_troca]=message.text


    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Retornar ao inicio', callback_data='inicio')
    but2 = types.InlineKeyboardButton('Mudar outro valor', callback_data='produto')
    markup.add(but1, but2)
    mensagem_botao_salva(bot,message,"Operação realizada com sucesso",markup)




bot.polling()
