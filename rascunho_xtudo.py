
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

with open("itens.json") as file:
    itens= json.load(file)





#---------------------------criar funções com as categorias produtos e itens--------------------------------



def lista_categorias():
    categorias=loja_data.keys()
    return categorias
def lista_produtos(categoria,chat_id):
    produtos={chat_id:loja_data.get(categoria,{}).keys()}

    return produtos[chat_id]

def lista_itens(categoria,produto):
    itens=loja_data[categoria][produto].get("Itens",[])
    return itens

categorias=lista_categorias()


#---------------------------Fim da criação das funções com as categorias produtos e itens--------------------------------

#--------------------------------criação da imagem-----------------------------------------------------------------------

imagem= open("cardapio.jpeg","rb")
#---------------------------mensagem inicial -------------------------------------------------------------------------
@bot.message_handler(func=lambda message: True)
def inicio(message):
 try:
    mensagem= message.message_id
    chat=message.chat.id
    print(chat)
    markup= telebot.types.InlineKeyboardMarkup(row_width=1)
    botao=telebot.types.InlineKeyboardButton("Fazer um pedido",callback_data="pedido")
    markup.add(botao)
    bot.send_message(chat,"Confira nosso catálogo")
    bot.send_photo(chat,imagem)
    bot.send_message(message.chat.id, " Seja bem vindo a nossa loja",reply_markup=markup)
    for x in range(mensagem,mensagem-5,-1):
       try:
        bot.delete_message(chat,x)
       except:
           pass

 except:
     mensagem = message.message_id
     chat = message.chat.id
     print(chat)
     markup1=telebot.types.InlineKeyboardMarkup(row_width=1)
     botao1=telebot.types.InlineKeyboardButton("Menu inicial", callback_data="inicio")
     markup1.add(botao1)
     bot.send_message(chat,"Algo deu errado , retorne ao início",reply_markup=markup1)
mensagem_acumulada_itens={}

# Essa vem dos menus retornar
@bot.callback_query_handler(func=lambda call: call.data=="inicio")
def inicio(call):
    mensagem= call.message.message_id
    chat=call.message.chat.id
    imagem1 = open("cardapio.jpeg", "rb")
    if chat in mensagem_acumulada_itens: # deleta a mensagem e insere None no acumulador

        bot.delete_message(chat,mensagem_acumulada_itens[chat])

        del mensagem_acumulada_itens[chat]

    markup= telebot.types.InlineKeyboardMarkup(row_width=1)
    botao=telebot.types.InlineKeyboardButton("Fazer um pedido",callback_data="pedido")
    markup.add(botao)
    bot.send_message(chat, "Confira nosso catálogo")
    bot.send_photo(chat, imagem1)
    bot.send_message(chat, " Seja bem vindo a nossa loja", reply_markup=markup)
    for x in range(mensagem, mensagem - 5, -1):
        try:
            bot.delete_message(chat, x)
        except:
            pass

#-------------------------------Escolha da categoria em que está o produto-----------------------------------------------

@bot.callback_query_handler(func= lambda call: call.data == "pedido")
def escolha_categoria(call):

    mensagem = call.message.message_id
    chat = call.message.chat.id



    markup=telebot.types.InlineKeyboardMarkup(row_width=1)
    for x in categorias:
     botao=telebot.types.InlineKeyboardButton(x,callback_data=x)
     markup.add(botao)
    bot.send_message(chat,"Escolha a categoria do produto", reply_markup=markup )
    for x in range(mensagem, mensagem - 5, -1):
        try:
            bot.delete_message(chat, x)
        except:
            pass


categoria_escolhida={} # dicionário criado com a categoria escolhida pelo cliente
produtos_da_categoria={} # dicionario criado com o id do cliente mais a lista de produtos da categoria escolhida


#------------------------------------escolha do produto -------------------------------------------------------------

# Aqui ocorrerá a escolha do produto
@bot.callback_query_handler(func= lambda call: call.data in categorias)
def escolha_produtos(call):
    global categoria_escolhida ,produtos_da_categoria
    mensagem = call.message.message_id
    chat = call.message.chat.id

    categoria_escolhida[chat]=call.data
    produtos_da_categoria=lista_produtos(call.data,chat) # lista dos produtos da categoria escolhida

    markup = telebot.types.InlineKeyboardMarkup(row_width=1) # Cria os botões com os produtos da categoria
    for x in produtos_da_categoria:
        botao = telebot.types.InlineKeyboardButton(x, callback_data=x)
        markup.add(botao)
    botao1=telebot.types.InlineKeyboardButton("Retornar ao Menu inicial", callback_data="inicio")
    markup.add(botao1)
    bot.send_message(chat, "Escolha o produto", reply_markup=markup) # Mensagem com para escolha dos botões


    for x in range(mensagem, mensagem - 5, -1):
        try:
            bot.delete_message(chat, x)
        except:
            pass

dicionario_itens_produto={} # listará os itens do produto  escolhidos pelo cliente para ser excluido
lista_itens_produto1=[] # lista dos itens escolhidos


produto_escolhido={} # produto escolhido
lista_produto={} # lista dos itens do produto escolhido

# --------------------------------- Cria a lista para escolha de seus itens------------------------------------------------------

@bot.callback_query_handler(func=lambda call: call.data in produtos_da_categoria)
def escolha_itens(call):
    global lista_produto , dicionario_itens_produto


    mensagem = call.message.message_id
    chat = call.message.chat.id



    produto_escolhido[chat]=call.data # acaba de receber o produto escolido atrelando ao id do chat
    dicionario_itens_produto[chat]=list() # aqui eu informo que ele recebera uma lista

    lista_produto[chat]=None # zerando a lista de produtos



    lista_produto[chat]=lista_itens(categoria_escolhida[chat], call.data) # cria lista com os itens do produto escolhido para caixa de seleção


    markup = telebot.types.InlineKeyboardMarkup(row_width=2) # cria o teclado dos itens
    for x in lista_produto[chat]: # for de criação do teclado
        botao = telebot.types.InlineKeyboardButton(x, callback_data=x)
        markup.add(botao)
    botao1 = telebot.types.InlineKeyboardButton("Retornar ao Menu inicial", callback_data="inicio")
    botao=telebot.types.InlineKeyboardButton("Prosseguir",callback_data="escolha_bebida")
    markup.add(botao1,botao)

    lista_mensagem=" - ".join(lista_produto[chat]) # Transforma a lista criada dos itens do produto em string
    bot.send_message(chat, f"Produto escolhido : {call.data}\nPossíveis acompanhamentos: {lista_mensagem} ")# mensagem dos itens do produto
    bot.send_message(chat, "Escolha os Itens que deseja remover do lanche ", reply_markup=markup) # mensagem que trará o teclado

    for x in range(mensagem, mensagem - 5, -1):
        try:
            bot.delete_message(chat, x)
        except:
            pass


# Aqui acrescentaremos os itens excluidos em um dicionário  para uso posterior
@bot.callback_query_handler(func=lambda call: call.data in itens)
def itens_escolha(call):
    global  dicionario_itens_produto, mensagem_acumulada_itens

    mensagem = call.message.message_id
    chat = call.message.chat.id


    if chat in mensagem_acumulada_itens: # deleta a mensagem e insere None no acumulador
        bot.delete_message(chat,mensagem_acumulada_itens[chat])
        del mensagem_acumulada_itens[chat]



    if call.data in dicionario_itens_produto[chat]: # lógica para acrescentar itens excluidos no pedido
        dicionario_itens_produto[chat].remove(call.data)
    else:
        dicionario_itens_produto[chat].append(call.data)
    lista= " - ".join(dicionario_itens_produto[chat])



    mensagem=bot.send_message(chat,f"Itens Excluidos : {lista}\n Deseja prosseguir"
                                   f" com o pedido? Caso ainda queira é só retirar mais itens") # dispara a mensagem e atribui  informações da mensagem
    mensagem_acumulada_itens[chat]=mensagem.message_id # recebe seu id





 #1 criar uma função  call.data=="escolha_bebida"
@bot.callback_query_handler(func=lambda call: call.data=="escolha_bebida")
def itens_escolha_bebida(call):
    mensagem = call.message.message_id
    chat = call.message.chat.id


    markup=telebot.types.InlineKeyboardMarkup(row_width=2)
    botao1=telebot.types.InlineKeyboardButton("Sim",callback_data="bebida_sim")
    botao2=telebot.types.InlineKeyboardButton("Não",callback_data="informe_pedido")
    markup.add(botao1,botao2)
    bot.send_message(chat,"Deseja incluir uma bebida ao pedido?",reply_markup=markup)
    for x in range(mensagem, mensagem - 5, -1):
        try:
            bot.delete_message(chat, x)
        except:
            pass


#Abertura da mensagem quando a bebida é escolhida como sim para ser adicionada
dicionario_bebida_escolhida={}
@bot.callback_query_handler(func=lambda call: call.data=="bebida_sim")
def bebida_sim1(call):
    global dicionario_bebida_escolhida

    mensagem = call.message.message_id
    chat = call.message.chat.id

    dicionario_bebida_escolhida[chat] = [] # Aqui é criado uma lista vazia para posteriores bebidas adicionadas

    if chat in mensagem_acumulada_itens: #  insere None no acumulador de mensagem  do item
        del mensagem_acumulada_itens[chat]


    markup=telebot.types.InlineKeyboardMarkup(row_width=2)# gera as bebidas com preço
    for x , y in  loja_data["Bebida"].items():
          botao=telebot.types.InlineKeyboardButton(f"{x} = {y} Reais",callback_data=x)
          markup.add(botao)
    botao1 = telebot.types.InlineKeyboardButton("Prosseguir", callback_data="informe_pedido")
    botao2= telebot.types.InlineKeyboardButton("Retornar ao Menu inicial", callback_data="inicio")
    markup.add(botao1,botao2)

    bot.send_message(chat,"Escolha as bebidas do pedido",reply_markup=markup)# mensagem para escolha da bebida


    for x in range(mensagem, mensagem - 5, -1):# Limpa a tela
        try:
            bot.delete_message(chat, x)
        except:
            pass

# Aqui é o local em que exibimos a mensagem das bebidas selecionadas e teremos o dicionário com as mesmas
mensagem_acumulada_bebida={}
@bot.callback_query_handler(func=lambda call: call.data in loja_data["Bebida"])
def itens_escolha(call):
    global  dicionario_bebida_escolhida, mensagem_acumulada_bebida

    mensagem = call.message.message_id
    chat = call.message.chat.id


    if chat in mensagem_acumulada_bebida: # deleta a mensagem e insere None no acumulador da bebida
        bot.delete_message(chat,mensagem_acumulada_bebida[chat])
        del mensagem_acumulada_itens[chat]



    if call.data in dicionario_bebida_escolhida[chat]: # lógica para acrescentar bebidas  no pedido
        dicionario_bebida_escolhida[chat].remove(call.data)
    else:
        dicionario_bebida_escolhida[chat].append(call.data)
    lista= " - ".join(dicionario_bebida_escolhida[chat])


    mensagem=bot.send_message(chat,f"Bebida escolhida : {lista}\n Deseja prosseguir"
                                   f" com o pedido? Caso ainda queira é só incluir mais bebidas") # dispara a mensagem e atribui  informações da mensagem
    mensagem_acumulada_bebida[chat]=mensagem.message_id # recebe seu id da mensagem

pedido={}
soma_produtos={}
@bot.callback_query_handler(func=lambda call: call.data=="informe_pedido")
def informe_pedido1(call):
    global produto_escolhido, categoria_escolhida,lista_produto, dicionario_bebida_escolhida,loja_data,pedido,soma_produtos

    mensagem = call.message.message_id
    chat = call.message.chat.id

    markup=telebot.types.InlineKeyboardMarkup(row_width=3)
    botao1=telebot.types.InlineKeyboardButton("Continuar com pedido",callback_data="endereco")
    botao2=telebot.types.InlineKeyboardButton("Cancelar pedido",callback_data="inicio")
    botao3=telebot.types.InlineKeyboardButton("Adicionar mais produtos",callback_data="inicio")
    markup.add(botao1,botao2,botao3)



    if chat in mensagem_acumulada_bebida: #  insere None no acumulador de mensagem  do item
        bot.delete_message(chat,mensagem_acumulada_bebida[chat])
        del mensagem_acumulada_bebida[chat]


    categoria=categoria_escolhida[chat] #variáveis acumuladoras dos valores
    produto = produto_escolhido[chat]

    valor_produto = loja_data[categoria][produto]["Valor"]
    valor_produto.replace(",",".")
    valor_produto=int(valor_produto)

    itens_produto=lista_produto[chat]
    for x in dicionario_itens_produto[chat] :
        if x in itens_produto:
            itens_produto.remove(x)
    itens_produto= "-".join(itens_produto)

    if dicionario_bebida_escolhida:
     bebida= "-".join(dicionario_bebida_escolhida[chat])
     valor_bebida=int()
     for a in dicionario_bebida_escolhida[chat]:
        valor_bebida+=loja_data["Bebida"][a]

     soma_produtos[chat]=valor_bebida+valor_produto

     bot.send_message(chat,f"------------Pedido------------\nProduto: {produto}= {valor_produto}\nAcompanhamento: {itens_produto}\nBebida: {bebida}= {valor_bebida}\n"
          f"Valor do pedido = {soma_produtos[chat]}",reply_markup=markup)
    else:
        soma_produtos[chat] = valor_produto

        bot.send_message(chat,
                         f"------------Pedido------------\nProduto: {produto}= {valor_produto}\nAcompanhamento: {itens_produto}\n"
                         f"Valor do pedido = {soma_produtos[chat]}",reply_markup=markup)
    for x in range(mensagem, mensagem - 5, -1):  # Limpa a tela
        try:
            bot.delete_message(chat, x)
        except:
            pass

# digitar o endereço para entrega

@bot.callback_query_handler(func=lambda call: call.data=="endereco")
def endereco1(call):
    mensagem = call.message.message_id
    chat = call.message.chat.id


    bot.send_message(chat,"Digite o endereço para entrega no campo da mensagem com o número da casa. Depois é só enviar")


    for x in range(mensagem, mensagem - 5, -1):  # Limpa a tela
        try:
            bot.delete_message(chat, x)
        except:
            pass

    bot.register_next_step_handler(call.message, observacao_final)

# função para adicionar observação
endereco={}
def observacao_final(message):
    global  endereco
    mensagem = message.message_id
    chat = message.chat.id

    endereco[chat]=message.text


    bot.send_message(chat,"Caso queira , deixe um comentário no campo de mensagem e depois envie ou clique em retornar")
    bot.register_next_step_handler(message, pagamento)

    for x in range(mensagem, mensagem - 5, -1):  # Limpa a tela
        try:
            bot.delete_message(chat, x)
        except:
            pass


observacao_final1={}
#Escolha da forma de pagamento
def pagamento(message):
    global observacao_final1
    mensagem = message.message_id
    chat = message.chat.id

    observacao_final1[chat] = message.text

    markup=telebot.types.InlineKeyboardMarkup(row_width=2)# Botão para escolha
    botao1=telebot.types.InlineKeyboardButton(text="Cartão",callback_data="pagamento_forma")
    botao2 = telebot.types.InlineKeyboardButton(text="Dinheiro", callback_data="pagamento_forma")
    markup.add(botao1,botao2)

    bot.send_message(chat,"Escolha a forma de pagamento: ", reply_markup=markup)
    for x in range(mensagem, mensagem - 5, -1):  # Limpa a tela
        try:
            bot.delete_message(chat, x)
        except:
            pass

# Depois da escolha da forma de pagamento
@bot.callback_query_handler(func=lambda call: call.data=="pagamento_forma")
def pagamento_forma1(call):
    mensagem = call.message.message_id
    chat = call.message.chat.id

    valor_botao = call.message.json['reply_markup']['inline_keyboard'][0][0]['text'] # Foma de obter o valor Cartão ou Dinheiro do botão
    global observacao_final1, categoria_escolhida, produto_escolhido, dicionario_itens_produto, dicionario_bebida_escolhida, soma_produtos

    if valor_botao=="Cartão": # Quando escolhido o cartão

        categoria = categoria_escolhida[chat]  # puxa a categoria escolhida
        produto = produto_escolhido[chat] # puxa o produto escolhido

        valor_produto = loja_data[categoria][produto]["Valor"] #valor do produto sendo transformado mais abaixo
        valor_produto.replace(",", ".")
        valor_produto = int(valor_produto)

        itens_produto = lista_produto[chat]# Contem a lista dos itens do produto
        for x in dicionario_itens_produto[chat]: # for para remover os itens excluidos
            if x in itens_produto:
                itens_produto.remove(x)
        itens_produto = "-".join(itens_produto)# Converte string  colocando - entre os nomes

        markup=telebot.types.InlineKeyboardMarkup(row_width=3) # teclado de escolha
        botao1=telebot.types.InlineKeyboardButton("Finalizar pedido",callback_data="enviar_pedido")
        botao2=telebot.types.InlineKeyboardButton("Refazer pedido",callback_data="inicio")

        if dicionario_bebida_escolhida:
            bebida = "-".join(dicionario_bebida_escolhida[chat])  # cria uma string com as bebidas escolhidas
            valor_bebida = int()  # variavel para somar valor das bebidas

            markup.add(botao1,botao2) #Cria o teclado com 2 opções

            for a in dicionario_bebida_escolhida[chat]:  # for para somatória do valor das bebidas

                valor_bebida += loja_data["Bebida"][a]
            bot.send_message(chat,
                                 f"------------Pedido------------\nProduto: {produto}= {valor_produto}\nBebida: {bebida}= {valor_bebida}\nAcompanhamento: {itens_produto}\n"
                                 f"Valor do pedido = {soma_produtos[chat]}\n------------Endereco------------\n\nEndereço: {endereco[chat]}\n\n"
                                 f"------------Observação------------\n\nObservação: {observacao_final1[chat]}\n\n"
                             f"------------Foma de pagamento------------\n\nPagamento: Cartão ",reply_markup=markup)

        else:
            soma_produtos[chat] = valor_produto

            markup.add(botao1, botao2)  # Cria o teclado com 2 opções

            bot.send_message(chat,
                             f"------------Pedido------------\nProduto: {produto}= {valor_produto}\nAcompanhamento: {itens_produto}\n"
                             f"Valor do pedido = {soma_produtos[chat]}\n------------Endereco------------\n\nEndereço: {endereco[chat]}\n\n"
                             f"------------Observação------------\n\nObservação: {observacao_final1[chat]}\n\n"
                             f"------------Foma de pagamento------------\n\nPagamento: Cartão  ",reply_markup=markup)

    else:



        categoria = categoria_escolhida[chat]  # variáveis acumuladoras dos valores
        produto = produto_escolhido[chat]

        valor_produto = loja_data[categoria][produto]["Valor"]
        valor_produto.replace(",", ".")
        valor_produto = int(valor_produto)

        itens_produto = lista_produto[chat]
        for x in dicionario_itens_produto[chat]:
            if x in itens_produto:
                itens_produto.remove(x)
        itens_produto = "-".join(itens_produto)

        if dicionario_bebida_escolhida: #Caso tenha bebida
            bebida = "-".join(dicionario_bebida_escolhida[chat])  # cria uma string com as bebidas escolhidas
            valor_bebida = int()  # variavel para somar valor das bebidas

            for a in dicionario_bebida_escolhida[chat]:  # for para somatória do valor das bebidas
                valor_bebida += loja_data["Bebida"][a]
            bot.send_message(chat,
                                 f"------------Pedido------------\nProduto: {produto}= {valor_produto}\nBebida: {bebida}= {valor_bebida}\nAcompanhamento: {itens_produto}\n"
                                 f"Valor do pedido = {soma_produtos[chat]}\n------------Endereco------------\n\nEndereço: {endereco[chat]}\n\n"
                                 f"------------Observação------------\n\nObservação: {observacao_final1[chat]}\n\n"
                                 f"------------Foma de pagamento------------\n\nPagamento: Dinheiro ")
            bot.send_message(chat,
                                 "Caso deseje troco , digite na mensagem o valor para o troco. Exemplo: Troco para 50,00 ou sem troco e envie")

        else:#Caso não tenha bebida
            soma_produtos[chat] = valor_produto
            bot.send_message(chat,
                             f"------------Pedido------------\nProduto: {produto}= {valor_produto}\nAcompanhamento: {itens_produto}\n"
                             f"Valor do pedido = {soma_produtos[chat]}\n------------Endereco------------\n\nEndereço: {endereco[chat]}\n\n"
                             f"------------Observação------------\n\nObservação: {observacao_final1[chat]}\n\n"
                             f"------------Foma de pagamento------------\n\nPagamento: Dinheiro ")
            bot.send_message(chat,
                             "Caso deseje troco , digite na mensagem o valor para o troco. Exemplo: Troco para 50,00 ou sem troco e envie")

    for x in range(mensagem, mensagem - 5, -1):  # Limpa a tela
        try:
            bot.delete_message(chat, x)
        except:
            pass


@bot.callback_query_handler(func=lambda call: call.data=="enviar_pedido")
def enviar_pedido1(call):
    mensagem = call.message.message_id
    chat = call.message.chat.id


    bot.send_message(chat,"Pedido finalizado com sucesso, obrigado pela preferência")


    categoria = categoria_escolhida[chat]  # puxa a categoria escolhida
    produto = produto_escolhido[chat]  # puxa o produto escolhido

    valor_produto = loja_data[categoria][produto]["Valor"]  # valor do produto sendo transformado mais abaixo
    valor_produto.replace(",", ".")
    valor_produto = int(valor_produto)

    itens_produto = lista_produto[chat]  # Contem a lista dos itens do produto
    for x in dicionario_itens_produto[chat]:  # for para remover os itens excluidos
        if x in itens_produto:
            itens_produto.remove(x)
    itens_produto = "-".join(itens_produto)  # Converte string  colocando - entre os nomes

    if dicionario_bebida_escolhida: # quando ha bebida
        bebida = "-".join(dicionario_bebida_escolhida[chat])  # cria uma string com as bebidas escolhidas
        valor_bebida = int()  # variavel para somar valor das bebidas

        for a in dicionario_bebida_escolhida[chat]:  # for para somatória do valor das bebidas
            valor_bebida += loja_data["Bebida"][a]
        bot.send_message(chat,
                         f"------------Pedido------------\nProduto: {produto}= {valor_produto}\nBebida: {bebida}= {valor_bebida}\nAcompanhamento: {itens_produto}\n"
                         f"Valor do pedido = {soma_produtos[chat]}\n------------Endereco------------\n\nEndereço: {endereco[chat]}\n\n"
                         f"------------Observação------------\n\nObservação: {observacao_final1[chat]}\n\n"
                         f"------------Foma de pagamento------------\n\nPagamento: Cartão ")

    else:
        soma_produtos[chat] = valor_produto

        bot.send_message(chat,
                         f"------------Pedido------------\nProduto: {produto}= {valor_produto}\nAcompanhamento: {itens_produto}\n"
                         f"Valor do pedido = {soma_produtos[chat]}\n------------Endereco------------\n\nEndereço: {endereco[chat]}\n\n"
                         f"------------Observação------------\n\nObservação: {observacao_final1[chat]}\n\n"
                         f"------------Foma de pagamento------------\n\nPagamento: Cartão  ")

    for x in range(mensagem, mensagem - 5, -1):  # Limpa a tela
        try:
            bot.delete_message(chat, x)
        except:
            pass






bot.polling()