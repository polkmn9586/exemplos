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



produtos_preco={}
produto_troca=""


ultima_mensagem_id=None
ultima_mensagem_id1=None
ultima_mensagem_id2=None
ultima_mensagem_id3=None

categoria=""  # servira para armazenar o nome de uma categoria  para uso
produto="" # servira para armazenar o nome de um produto  para uso
valor="" # servira para armazenar o valor de um produto  para uso

itens_geral=[] # essa lista é a lista geral dos itens
itens="" # esse elemento será usado na transformação dos itens em set e depois em str
item_excluido=""# item que será excluido

message_ids=[]
categoria_excluida=""
categoria_exclui_produto="" # Usado para armazenar a categoria da onde se encontra o produto ou o item a ser excluido
produto_excluido=""#produto da exclusão

categoria_exclui_item="" # Usado para armazenar o produto a onde se encontra o item a ser excluido
produto_exclui_item="" # item da exclusão
dados=lendo_arquivo_json_dic("loja.json") # Leitura do arquivo json carregando a variável dados






# ------------------------Define um manipulador de mensagem para o comando /limpar--------------------------

acumulador="" # receberá a message da função a seguir
@bot.callback_query_handler(func=lambda call: call.data=="limpar")
def limpar_tela(call):

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
        texto += f"--------Categoria: {categoria}--------\n\n"
        for produto, info in produtos.items():
            texto += f"Produto: {produto}\n"
            texto += f"Valor: {info['Valor']}\n"
            texto += f"Itens: {', '.join(info['Itens'])}\n\n"


    mensagem_botao_salva_1botao_call(bot,call,texto,"Menu iniciar","inicio")
    bot.delete_message(call.message.chat.id, call.message.message_id)



#-----------------------------------------texte----------------------------------------------------




#-----------------------------------------Mensagens iniciais----------------------------------------------------


#Mensagem inicial ao escrever algo na tela
@bot.message_handler(func=lambda message: True)
def inicio(message):
    global ultima_mensagem_id,ultima_mensagem_id2,ultima_mensagem_id1,ultima_mensagem_id4,ultima_mensagem_id5

    #ultima_mensagem_id = message.message_id # recebe a mensagem que acionou essa função

    markup = types.InlineKeyboardMarkup()  # Criação do teclado menu inicial
    but2 = types.InlineKeyboardButton('Criar categoria, produto ou item', callback_data='criar')
    but4 = types.InlineKeyboardButton('excluir: categoria , produto ou item', callback_data='excluir')
    but1 = types.InlineKeyboardButton('Imprimir catálogo', callback_data='mensagem')
    but3 = types.InlineKeyboardButton('Limpar a tela', callback_data='limpar')
    markup.add(but3)
    markup.add(but2)
    markup.add(but4)  # Incorporando os botões
    markup.add(but1)

    mensagem_botao_salva(bot, message,
                                                   "--------------------Configuração--------------------",
                                                   markup)  # Mensagem com o teclado e a atualização da id da

    apaga_mensagem(bot,message)
    if ultima_mensagem_id5 != None:
        ultima_mensagem_id5 = apaga_mensagem_id(bot, message, ultima_mensagem_id5)




#Mensagem inicial ao clicar em retornar
ultima_mensagem_id6=None
@bot.callback_query_handler(func=lambda call: call.data=="inicio")
def inicio(call):

      global ultima_mensagem_id,ultima_mensagem_id2,ultima_mensagem_id1,ultima_mensagem_id3,ultima_mensagem_id6,last_message


      markup = types.InlineKeyboardMarkup()  # Criação do teclado menu inicial
      but2 = types.InlineKeyboardButton('Criar categoria, produto ou item', callback_data='criar')

      but4 = types.InlineKeyboardButton('excluir: categoria , produto ou item', callback_data='excluir')
      but1 = types.InlineKeyboardButton('Imprimir catálogo', callback_data='mensagem')
      but3 = types.InlineKeyboardButton('Limpar a tela', callback_data='limpar')
      markup.add(but3)
      markup.add(but2)

      markup.add(but4)  # Incorporando os botões
      markup.add(but1)
      ultima_mensagem_id6=mensagem_botao_salva_call(bot, call, "--------------------Configuração--------------------",
                                                     markup)

      apaga_mensagem_call(bot, call)  # Apaga a mensagem do call
      if ultima_mensagem_id1 != None:
          ultima_mensagem_id1=apaga_mensagem_id_call(bot,call,ultima_mensagem_id1)

      if ultima_mensagem_id != None:
          ultima_mensagem_id=apaga_mensagem_id_call(bot,call,ultima_mensagem_id)

      if ultima_mensagem_id2 != None:
          ultima_mensagem_id2=apaga_mensagem_id_call(bot,call,ultima_mensagem_id2)

      if last_message:
              bot.delete_message(call.message.chat.id, last_message.message_id)
              last_message=None
      print(last_message)
def inicio1(message):
    global ultima_mensagem_id, ultima_mensagem_id2, ultima_mensagem_id1

    markup = types.InlineKeyboardMarkup()  # Criação do teclado menu inicial
    but2 = types.InlineKeyboardButton('Criar categoria, produto ou item', callback_data='criar')

    but4 = types.InlineKeyboardButton('excluir: categoria , produto ou item', callback_data='excluir')
    but1 = types.InlineKeyboardButton('Imprimir catálogo', callback_data='mensagem')
    but3 = types.InlineKeyboardButton('Limpar a tela', callback_data='limpar')
    markup.add(but3)
    markup.add(but2)

    markup.add(but4)  # Incorporando os botões
    markup.add(but1)
    mensagem_botao_salva(bot, message, "--------------------Configuração--------------------",
                              markup)

    apaga_mensagem(bot, message)  # Apaga a mensagem do call
    if ultima_mensagem_id1 != None:
        ultima_mensagem_id1 = apaga_mensagem_id(bot, message, ultima_mensagem_id1)

    if ultima_mensagem_id != None:
        ultima_mensagem_id = apaga_mensagem_id(bot, message, ultima_mensagem_id)

    if ultima_mensagem_id2 != None:
        ultima_mensagem_id2 = apaga_mensagem_id(bot, message, ultima_mensagem_id2)


#--------------iniciar a exclusão de uma categoria / produto / item------------------------------------------------------


# Aqui a escolha do que será excluido
@bot.callback_query_handler(func=lambda call: call.data == 'excluir')
def exclusao(call):
    global ultima_mensagem_id
    mensagem_botao_salva_call_3botoes(bot,call,"O que deseja excluir?","Categoria","Produtos","Itens","excluir_categorias","excluir_produtos","excluir_itens")
    apaga_mensagem_call(bot, call)


                 # ---------------------inicio da exclusão da categoria------------------------------

#Aqui ocorre a escolha da categoria que será excluida
ultima_mensagem_id12=""
@bot.callback_query_handler(func=lambda call: call.data == 'excluir_categorias')
def exclusao(call):
 global ultima_mensagem_id12

 keyboard=cria_caixa_selecao(dados)
 if dados == {} or None:

    mensagem_botao_salva_1botao_call(bot,call,"Você não possui nenhuma categoria cadastrada","Menu inicial","inicio")
    apaga_mensagem_call(bot, call)

 else:
     ultima_mensagem_id12=mensagem_botao_salva_call(bot, call, "Escolha a categoria que será excluida",keyboard)
     apaga_mensagem_call(bot, call)
     bot.register_next_step_handler(call.message, excluir_categoria)

# Pedido de confirmação da exclusão da categoria
def excluir_categoria(message):

    global categoria_excluida,ultima_mensagem_id12


    categoria_excluida=message.text #Recebe o que será excluído
    mensagem_botao_salva_2botoes(bot,message,f"Voce confirma a exclusão de: {message.text} ","Sim","Não","sim_excluir_categoria","inicio")
    apaga_mensagem_id(bot,message,ultima_mensagem_id12)
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




# ------------------------------------Inicio da exclusão do produto--------------------------------------------------




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


#----------------------------------------Fim da exclusão de um produto-------------------------------------------------------




#----------------------------------------Inicio da exclusão de um item-------------------------------------------------------


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


#----------------------------------------Fim da exclusão de um item-------------------------------------------------------


#-----------------------------------iniciar a criação de uma categoria / produto/ item------------------------------------------

# pergunta o que quer criar, produto ou categoria
@bot.callback_query_handler(func=lambda call: call.data == 'criar')
def botao_clicado4(call):
     global ultima_mensagem_id1,ultima_mensagem_id2

     markup = telebot.types.InlineKeyboardMarkup() #criação da janela do botões
     bot1= types.InlineKeyboardButton('Categoria', callback_data='cria_categoria')
     bot2 = types.InlineKeyboardButton('Produto', callback_data='cria_produto')
     bot4 = types.InlineKeyboardButton('Item', callback_data='criar_item')
     bot3 =types.InlineKeyboardButton('Retornar', callback_data='inicio')
     markup.add(bot1,bot2,bot4,bot3)
     mensagem_botao_salva_call(bot,call," Deseja criar? ",markup)
     apaga_mensagem_call(bot,call)




      #----------------------------------------Inicio da criação  de uma categoria-------------------------------------------------------

# Aqui é o momento aonde digitamos o nome da categoria

@bot.callback_query_handler(func=lambda call: call.data == 'cria_categoria')
def botao_clicado1(call):

         global ultima_mensagem_id,ultima_mensagem_id1,ultima_mensagem_id2,ultima_mensagem_id3

         categoria_arquivo=lendo_arquivo_json_dic("loja.json")
         categoria_lista=""
         for i in categoria_arquivo:
            categoria_lista+=f"{i}\n"

         ultima_mensagem_id=mensagem_botao_salva_call(bot,call,f"Categoris salvas:\n\n{categoria_lista}")
         ultima_mensagem_id3=mensagem_botao_salva_1botao_call(bot,call,"Digite o nome da categoria na mensagem e clique em enviar ou "
                                                               "clique em 'Retornar' para o Menu inicial","Retornar","inicio")

         #apaga_mensagem_call(bot, call)#Apaga a mensagem do call
         bot.register_next_step_handler(call.message, adic_categoria1) # Avança para uma função determinada independente
                                                                      # da escrita

#Função que cria a categoria
ultima_mensagem_id4=None # Usado para apagar a ultima mensagem caso entre e no except
ultima_mensagem_id5=None# # Usado para apagar a mensagem  do except será pagada no menu inicial
def adic_categoria1(message):

 global ultima_mensagem_id,ultima_mensagem_id1,ultima_mensagem_id2,ultima_mensagem_id3,dados,ultima_mensagem_id4
 try:
    if dados == {} or None:
        dados={message.text:{}}
    else:
     dados[message.text] = {} # Aqui eu crio em dados um key com o nome da minha categoria com None

    escrevendo_json_novo(dados,"loja.json")

    markup  = types.InlineKeyboardMarkup()
    botao1 = types.InlineKeyboardButton('continuar criando', callback_data='cria_categoria')
    botao2 = types.InlineKeyboardButton('retornar ao início', callback_data='inicio')
    markup.add(botao1,botao2)
    ultima_mensagem_id4=mensagem_botao_salva(bot,message,f"Categoria criada com sucesso: {message.text}",markup)

    apaga_mensagem(bot, message)  # Apaga a mensagem do call

    if ultima_mensagem_id !=None:
      ultima_mensagem_id=apaga_mensagem_id(bot,message,ultima_mensagem_id)

    if ultima_mensagem_id1 != None:
      ultima_mensagem_id1=apaga_mensagem_id(bot, message,ultima_mensagem_id1)

    if ultima_mensagem_id2 != None:
        ultima_mensagem_id2 = apaga_mensagem_id(bot, message, ultima_mensagem_id2)

    if ultima_mensagem_id3 != None:
        ultima_mensagem_id3 = apaga_mensagem_id(bot, message, ultima_mensagem_id3)
 except:
     mensagem_botao_salva_2botoes(bot,message,"Categoria criada com sucesso. ","Continuar cadastrando", "Menu inicial","cria_categoria","inicio")
     apaga_mensagem_id(bot,message,ultima_mensagem_id4)
     apaga_mensagem_id(bot, message, ultima_mensagem_id4-1)
     


#-----------------------------------Fim da criação de uma categoria-------------------------------------------------


#----------------------------------------Inicio da criação  de itens--------------------------------------------------


# Aqui é o momento aonde digitamos os nomes dos itens
ultima_mensagem_id6=None
@bot.callback_query_handler(func=lambda call: call.data == 'criar_item')
def criar_item1(call):

    global itens_geral,itens,ultima_mensagem_id1,ultima_mensagem_id,ultima_mensagem_id6

    itens_geral=lendo_arquivo_json_dic("itens.json") # leitura do arquivo em itens
    itens=set(itens_geral)# eliminando repetição com set em itens
    itens=list(itens) # tornando itens em list para poder ser gravado em json

    recebe1=""
    for i in itens: # For para criar uma string dos nomes dos itens
        recebe1+=f"{i}\n"

    ultima_mensagem_id1=mensagem_botao_salva_call(bot,call,f"Itens já cadastrados:\n{recebe1}")# imprimi itens já cadastrados

    apaga_mensagem_call(bot,call)

    ultima_mensagem_id6=mensagem_botao_salva_1botao_call(bot, call, "Digite no campo de mesagens os nomes dos itens que "
                                                              "deseja criar separando-os com "
                                                              "espaço e se forem compostos"
                                                              " escreva assim: cachorro-quente "
                                                              "e depois é so enviar, ou clique em retornar para o menu inicial"
                                                              "","Retornar","inicio")

    bot.register_next_step_handler(call.message, adic_item)  # Avança para uma função determinada independente
    # da escrita

# Aqui iremos armazenar os nomes dos itens em um set

def adic_item(message):

        global ultima_mensagem_id1,ultima_mensagem_id6,itens
        itens_temporario=message.text # Recebe os elementos que serão inseridos na lista
        itens_temporario=itens_temporario.split() # transforma a str digitada em lista
        itens_temporario=set(itens_temporario)# Trnsforma em set para eliminar repetições
        itens=set(itens)# Transforma em set , pois não estava sendo reconhecido
        for i in itens_temporario: # loop para adicionar novos elementos em itens
            itens.add(i.upper().strip()) # Eliminando espaços e colocando em maiusculas

        escrevendo_json_novo(itens,"itens.json")# Escrita  em json


        itens_impressao=str(itens_temporario) # transforma a lista digitada em str para imprimir
        itens_impressao=itens_impressao.replace("{"," ").replace("}"," ").replace("'"," ")#Remove os elementos indesejáveis para impressão

        mensagem_botao_salva_2botoes(bot,message, f"Itens que acabou de cadastrar:\n{itens_impressao}",
                                     "Menu inicial","Continuar cadastrando","inicio",'criar_item')

        apaga_mensagem(bot,message) # Apaga a ultima mensagem

        if ultima_mensagem_id1 != None: # Apagará as ultimas mensagens caso existam
           ultima_mensagem_id1= apaga_mensagem_id(bot,message, ultima_mensagem_id1) # ela precisa ser adicionada a ultima
        if ultima_mensagem_id6 != None:  # Apagará as ultimas mensagens caso existam
           ultima_mensagem_id6 = apaga_mensagem_id(bot, message, ultima_mensagem_id6)
           # para torna-la nula


#-------------------------------------Fim da criação de itens------------------------------------------------








#----------------------------------------Inicio da criação de um produto-------------------------------------------------------


#Essa função será chamada no momento em que se tenta criar um produto ou um produto sem uma categoria
ultima_mensagem_id9=""
@bot.callback_query_handler(func=lambda call: call.data == 'cria_produto')
def botao_clicado3(call):
        global ultima_mensagem_id9

        if dados == {} or None: # Caso do loja.json vazio

            markup = telebot.types.InlineKeyboardMarkup()
            botao1 = telebot.types.InlineKeyboardButton('Retorne', callback_data='inicio')
            markup.add(botao1)
            mensagem_botao_salva_call(bot, call, "Você ainda não possui uma categoria cadastrada , "
                                                 "precisa cadastrar uma para adicionar um produto nela", markup)
        else:


            lista = [x for x in dados]  # criação da lista de seleção com as categoria,escolher a categoria aonde se encontra o produto
            keyboard = ReplyKeyboardMarkup(
                row_width=1)  # utilizando a lista para criar com os seus itens uma caixa de seleção

            for opcao in lista:     # esse for é rodado na lista das categorias adicionando ao teclado o nome das categorias ,
                                    # para que possam ser escolhidas
                keyboard.add(opcao)


            ultima_mensagem_id9=mensagem_botao_salva_call(bot, call, "Escolha a categoria que deseja incluir seu produto", keyboard)
            apaga_mensagem_call(bot,call)
            bot.register_next_step_handler(call.message, cria_produto_escoha_categoria)


#Aqui será digitado o nome do produto e salva a categoria

ultima_mensagem_id7=""
ultima_mensagem_id10=""
def cria_produto_escoha_categoria(message):

    global ultima_mensagem_id7,ultima_mensagem_id9,categoria,ultima_mensagem_id10

    categoria = message.text # armazenando valor em categoria para ser usado na proxima função
    dicionario=lendo_arquivo_json_("loja.json") # possui o documento nessa variável
    lista = ""
    resultado=""
    for x in dicionario.keys():
        if dicionario[x] != {}:
            casa1 = dicionario[x]
            lista += f"{x}: "
            for b in casa1:
                lista += f"{b}, "
            lista += "\n"
            resultado += lista

    ultima_mensagem_id10=mensagem_botao_salva(bot,message,f"Produtos cadastrados:\n {resultado}")
    resultado=""
    ultima_mensagem_id7=apaga_janela_selecao(bot, message, "Digite o nome do produto que deseja cadastrar")
    apaga_mensagem(bot, message)
    apaga_mensagem_id(bot,message,ultima_mensagem_id9)


    bot.register_next_step_handler(message, digite_produto)

#Aqui será digitado o valor do produto e salvo o nome do produto

ultima_mensagem_id8=""
def digite_produto(message):

    global ultima_mensagem_id7,ultima_mensagem_id8, produto
    produto = message.text # armazenando o nome  do novo produto para ser usado na proxima função

    ultima_mensagem_id8=mensagem_botao_salva(bot, message, "Digite o valor do produto")
    apaga_mensagem(bot,message)
    apaga_mensagem_id(bot,message,ultima_mensagem_id7)
    bot.register_next_step_handler(message, handle_start)


# Nessa função será armazenado o valor do produto e feita a escolha do item em uma lista geral ou a criação

lista1 = lendo_arquivo_json_("itens.json")

def generate_markup():
    markup = types.InlineKeyboardMarkup()
    for item in lista1:
        markup.add(types.InlineKeyboardButton(text=item, callback_data=item))
    markup.add(types.InlineKeyboardButton(text="Retornar", callback_data="inicio"))
    markup.add(types.InlineKeyboardButton(text="Prosseguir", callback_data="produto_iten"))
    return markup


def handle_start(message):
    global ultima_mensagem_id8, valor, itens_geral,lista1
    lista1 = lendo_arquivo_json_("itens.json")
    valor = message.text  # armazenando o valor do produto para ser usado na proxima função
    markup = generate_markup()
    apaga_mensagem(bot,message)

    bot.send_message(message.chat.id, "Escolha os itens que estarão no produto. Cique Retornar para ir para o menu "
                                      "inicial e Prosseguir para continuar o cadastro do produto", reply_markup=markup)
    apaga_mensagem_id(bot, message, ultima_mensagem_id8)


lista_itens = []
last_message = None

ultima_mensagem_id11=""
@bot.callback_query_handler(func=lambda call: call.data in lista1)
def handle_query(call):
   #try:
    global lista_itens, last_message,ultima_mensagem_id11
    item_escolhido = call.data
    if item_escolhido in lista_itens:
        lista_itens.remove(item_escolhido)
    else:
        lista_itens.append(item_escolhido)
    if last_message:
        bot.delete_message(call.message.chat.id, last_message.message_id)
    last_message = bot.send_message(call.message.chat.id, "Itens escolhidos: " + ', '.join(lista_itens))

   #except:
       #mensagem_botao_salva_1botao_call(bot,call,"Algo deu errado , por favor retornar ","Retornar","inicio")


@bot.callback_query_handler(func=lambda call: call.data == 'produto_iten')
def produto_itens1(call):

    global  dados,lista_itens,categoria,lista1,last_message



    markup = telebot.types.InlineKeyboardMarkup()
    botao1 = telebot.types.InlineKeyboardButton('Continuar', callback_data='cria_produto')
    botao2 = telebot.types.InlineKeyboardButton('Menu inicial', callback_data='inicio')
    markup.add(botao1,botao2)

    if dados[categoria]==None: # se for None ele precisa indicar que o próximo elemento é um dic, depois dessa
                               # indicação os demais serão reconhecidos como dic

      dados[categoria]={produto:{"Valor":valor,"Itens":lista_itens}} # Forma para reconhecer como dic

      escrevendo_json_novo(dados,"loja.json")
    else:
     dados[categoria][produto]= {"Valor": valor, "Itens": lista_itens} # Aqui já reconhecido como dic

     escrevendo_json_novo(dados, "loja.json")

    apaga_mensagem_call(bot,call)
    mensagem_botao_salva_call(bot, call, f"Cadastro:"
                                       f"\nCategoria: {categoria}"
                                       f"\nProduto: {produto}"
                                       f"\nValor: {valor}"
                                       f"\nItens: {lista_itens}"
                                       f"\nPara continuar cadastrando produto clique em continuar",markup)
    if ultima_mensagem_id10:
     apaga_mensagem_id_call(bot,call,ultima_mensagem_id10)


    lista_itens=[]


#----------------------------------fim-------------------------------------------------------------------------

# Chamada pelo final da mudança do valor do produto



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
