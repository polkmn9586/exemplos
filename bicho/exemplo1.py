from itertools import groupby
import json
import math
from datetime import datetime,timedelta
from datetime import datetime
from dateutil import relativedelta
import sys
from PySide6.QtCore import Slot,Qt
from random import randint, sample
from PySide6.QtWidgets import QApplication,QMainWindow, QWidget,QGridLayout,QPushButton,QLineEdit,QLabel,QTextEdit,QCheckBox,QComboBox,QButtonGroup
import sys

from ast import literal_eval
import re
from programa_do_bicho2 import Ui_Form
from criador import Criador
from PySide6.QtGui import QIcon

from pathlib import Path



with open("bicho.json","r") as arquivo:
    dados=json.load(arquivo)

dicionário={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0}
lista1={2,4,5}


def bicho(lista1,maior,menor):
    """Pega uma lista de grupos e retorna um dicionário com os grupos mais prováveis"""
    #---------------------------------------------------------------------------------------------------
    # Criando 25 bichos com  0 para iniciar o valor de cada um
    # Resultado estará em dicionario_de_bichos
    lista=lista1
    print(lista)
    dicionario_de_bichos={}
    #------------------------------------lógica---------------------------------------------------------
    cont=1
    for x in range(25):
        dicionario_de_bichos.update({cont:0})
        cont+=1


    #-----------------------------------------------------------------------------------------------
    # Vai passar pelos elementos da lista adicionando atraso e retirando atraso do dicionário
    # O resultado estará em dicionario_de_bichos
    cont = 1

    for sorteado in lista:
        for lista_de_bicho in dicionario_de_bichos:

    #------------------------------------------lógica--------------------------------------------------

            if lista_de_bicho==sorteado:

               dicionario_de_bichos[sorteado]=0

            else:
                dicionario_de_bichos[lista_de_bicho]+=1

        cont+=1

    cont=0

    #-----------------------------------------------------------------------------------------------------
    #Aqui se filtra bichos prováveis para escolha , lembrando que ele rodará em uma lista já formada e não
    # está caminhando passo a passo, para isso teriamos que colocar essa lógiga no passo a passo em que os
    # bichos vão sendo adicionado atrasos.
    bicho_provavel={}
    for bicho , atraso in dicionario_de_bichos.items():

    #---------------------------------Lógica---------------------------------------------------------------
        if atraso>=int(menor) and atraso <=int(maior):

            if bicho_provavel:

              bicho_provavel.update({bicho:atraso})
            else:
                bicho_provavel={bicho: atraso}


    return bicho_provavel

def treino_grupos_sorteados_juntos(self,lista,menor=30,maior=35,quantidade=5):
    try:
        lista1, lista2, lista3, lista4, lista5 = lista
        contador=0
        menor = menor
        maior = maior
        recebe = []
        cont = 10
        cont_jogos=0
        acertos = int()
        total_jogos_jogados = int()
        quantidade=int(quantidade)
        self.textEdit.setText("")
        bicho_provavel_temporario_set = set()
    except:
        self.textEdit.setText("Algo deu errado, o preenchimento do campo é obrigatório")


    # -----------------------------------------------------------------------------------------------------
    #Vamos caminhar passo a passo entre a lista dos 5 sorteios
    if cont>len(lista1):

        #Mensagem caso seja escolhido menos de 10 jogos----------------------------------
        self.textEdit.setText("Escolha pelo menos 10 jogos")
        self.lineEdit_4.setText("Escolha pelo menos 10 jogos")

    #Vamos percorrer todos os sorteios de cada jogo-----------------------------------------
    while cont <= len(lista1):
        self.textEdit.setText("")
        self.lineEdit_4.setText("")

        lista_provisoria = []
        numeros_sorteados = []
        bicho_provavel_temporario={}



        try:
    #-----------------------------------------------------------------------------------------------------
      # temos aqui os possíveis bicho de sairem nesse momento no primeiro sorteio, aqui está ocorrendo passo a passo
            lista_provisoria=lista1[:cont]

            bicho_provavel_temporario=bicho(lista_provisoria,maior,menor)

            bicho_provavel_temporario_set=set()
            bichos_sorteados=set()

        #--------------------------------------------------------------------------------------------
          #Carregando os bichos em uma lista de str e depois convertendo em lista int, lista dos bichos possiveis
            if bicho_provavel_temporario:
                for bicho_tupla in bicho_provavel_temporario:
                      bicho_provavel_temporario_set.add(bicho_tupla)


        #--------------------------------------------------------------------------------------------

    #------------------------------------------------------------------------------------------------------
    #Aqui vamos pegar o número atual da lista1 e conferir com os números possíveis

            bichos_sorteados.add(lista1[cont])


            #input("Enter ")

        except:



            ...

        try:

            lista_provisoria = lista2[:cont]
            bicho_provavel_temporario = bicho(lista_provisoria,maior,menor)


            # --------------------------------------------------------------------------------------------
            # Carregando os bichos em uma lista de str e depois convertendo em lista int, lista dos bichos possiveis
            if bicho_provavel_temporario:
                for bicho_tupla in bicho_provavel_temporario:
                    bicho_provavel_temporario_set.add(bicho_tupla)


            # --------------------------------------------------------------------------------------------

            # ------------------------------------------------------------------------------------------------------
            # Aqui vamos pegar o número atual da lista1 e aceita-lo caso o seu atraso tenha o tempo aceito colocando em
            # numeros_sorteados

            bichos_sorteados.add(lista2[cont])


            #input("Enter 2")

        except:
            ...


        try:

            lista_provisoria = lista3[:cont]
            bicho_provavel_temporario = bicho(lista_provisoria,maior,menor)


            # --------------------------------------------------------------------------------------------
            # Carregando os bichos em uma lista de str e depois convertendo em lista int, lista dos bichos possiveis
            if bicho_provavel_temporario:
                for bicho_tupla in bicho_provavel_temporario:
                    bicho_provavel_temporario_set.add(bicho_tupla)


            # --------------------------------------------------------------------------------------------

            # ------------------------------------------------------------------------------------------------------
            # Aqui vamos pegar o número atual da lista1 e aceita-lo caso o seu atraso tenha o tempo aceito colocando em
            # numeros_sorteados

            bichos_sorteados.add(lista3[cont])


            #input("Enter 3")

        except:
            ...
        try:

            lista_provisoria = lista4[:cont]
            bicho_provavel_temporario = bicho(lista_provisoria,maior,menor)


            # --------------------------------------------------------------------------------------------
            # Carregando os bichos em uma lista de str e depois convertendo em lista int, lista dos bichos possiveis
            if bicho_provavel_temporario:
                for bicho_tupla in bicho_provavel_temporario:
                    bicho_provavel_temporario_set.add(bicho_tupla)


            # --------------------------------------------------------------------------------------------

            # ------------------------------------------------------------------------------------------------------
            # Aqui vamos pegar o número atual da lista1 e aceita-lo caso o seu atraso tenha o tempo aceito colocando em
            # numeros_sorteados

            bichos_sorteados.add(lista4[cont])


          #  input("Enter 4")

        except:
            ...
        try:
            lista_provisoria = lista5[:cont]
            bicho_provavel_temporario = bicho(lista_provisoria,maior,menor)


            # --------------------------------------------------------------------------------------------
            # Carregando os bichos em uma lista de str e depois convertendo em lista int, lista dos bichos possiveis
            if bicho_provavel_temporario:
                for bicho_tupla in bicho_provavel_temporario:
                    bicho_provavel_temporario_set.add(bicho_tupla)


            # --------------------------------------------------------------------------------------------

            # ------------------------------------------------------------------------------------------------------
            # Aqui vamos pegar o número atual da lista1 e aceita-lo caso o seu atraso tenha o tempo aceito colocando em
            # numeros_sorteados

            bichos_sorteados.add(lista5[cont])

            #input("Enter 5")


        except:
           ...

        try:



            self.radio_group = QButtonGroup(self)
            self.radio_group.addButton(self.radioButton_8, id=3)
            self.radio_group.addButton(self.radioButton_9, id=4)
            check_modo = int(self.radio_group.checkedId())
            soma=0
            if len(bicho_provavel_temporario_set) >2 and len(bicho_provavel_temporario_set)<=quantidade:

                #Imprimindo bichos para o proximo sorteio--------------------------------------------------
                self.lineEdit_4.setText(str(bicho_provavel_temporario_set))

                #Conferindo os bichos dados com alista de possíveis--------------------------------------------------------------
                for confere in bichos_sorteados:
                    if confere in bicho_provavel_temporario_set:
                        soma+=1
                if soma>=check_modo:
                    acertos+=1

                cont_jogos += 1
            else:
                self.lineEdit_4.setText("Não possui jogos para os valores informados")
            cont += 1
        except:
            self.textEdit.setText("Precisa preencher corretamente os campos")
            cont += 1
    total_jogos_jogados=cont_jogos
    total_de_jogos=cont-9
    self.textEdit.setText(f"Quantidade de jogos: {total_de_jogos}\n"
                          f"Quantidade de jogos jogados: {total_jogos_jogados}\n"
                          f"Quantidade de acertos: {acertos}")

def grupos_provaveis(self, lista, menor=30, maior=35, quantidade=5):
    try:
        lista1, lista2, lista3, lista4, lista5 = lista
        contador = 0
        menor = menor
        maior = maior
        recebe = []
        cont = 10
        cont_jogos = 0
        acertos = int()
        total_jogos = int()
        quantidade = int(quantidade)
        self.textEdit.setText("")
        bicho_provavel_temporario_set = set()
    except:

        self.lineEdit_4.setText("Algo deu errado, o preenchimento do campo é obrigatório")

    # -----------------------------------------------------------------------------------------------------
    # Vamos caminhar passo a passo entre os 5 sorteios
    if cont > len(lista1):

        # Mensagem caso seja escolhido menos de 10 jogos----------------------------------
        self.lineEdit_4.setText("Escolha pelo menos 10 jogos")

    # Vamos percorrer todos os sorteios de cada jogo-----------------------------------------
    while cont <= len(lista1):

        self.lineEdit_4.setText("")

        lista_provisoria = []
        numeros_sorteados = []
        bicho_provavel_temporario = {}

        try:
            # -----------------------------------------------------------------------------------------------------
            # temos aqui os possíveis bicho de sairem nesse momento no primeiro sorteio, aqui está ocorrendo passo a passo
            lista_provisoria = lista1[:cont+1]
            bicho_provavel_temporario = bicho(lista_provisoria, maior, menor)
            bicho_provavel_temporario_set = set()


            # --------------------------------------------------------------------------------------------
            # Criando um set com os bichos prováveis temporários
            if bicho_provavel_temporario:
                for bicho_tupla in bicho_provavel_temporario:
                    bicho_provavel_temporario_set.add(bicho_tupla)



        except:

            ...

        try:

            lista_provisoria = lista2[:cont+1]
            bicho_provavel_temporario = bicho(lista_provisoria, maior, menor)

            # --------------------------------------------------------------------------------------------
            # Criando um set com os bichos prováveis temporários
            if bicho_provavel_temporario:
                for bicho_tupla in bicho_provavel_temporario:
                    bicho_provavel_temporario_set.add(bicho_tupla)



        except:
            ...

        try:

            lista_provisoria = lista3[:cont+1]
            bicho_provavel_temporario = bicho(lista_provisoria, maior, menor)

            # --------------------------------------------------------------------------------------------
            # Criando um set com os bichos prováveis temporários
            if bicho_provavel_temporario:
                for bicho_tupla in bicho_provavel_temporario:
                    bicho_provavel_temporario_set.add(bicho_tupla)



        except:
            ...
        try:

            lista_provisoria = lista4[:cont+1]
            bicho_provavel_temporario = bicho(lista_provisoria, maior, menor)

            # --------------------------------------------------------------------------------------------
            # Criando um set com os bichos prováveis temporários
            if bicho_provavel_temporario:
                for bicho_tupla in bicho_provavel_temporario:
                    bicho_provavel_temporario_set.add(bicho_tupla)



        except:
            ...
        try:
            lista_provisoria = lista5[:cont+1]
            bicho_provavel_temporario = bicho(lista_provisoria, maior, menor)

            # --------------------------------------------------------------------------------------------
            # Criando um set com os bichos prováveis temporários
            if bicho_provavel_temporario:
                for bicho_tupla in bicho_provavel_temporario:
                    bicho_provavel_temporario_set.add(bicho_tupla)


        except:
            ...

        try:


            self.radio1_group = QButtonGroup(self)
            self.radio1_group.addButton(self.radioButton_7, id=3)
            self.radio1_group.addButton(self.radioButton_6, id=4)

            check_modo=self.radio1_group.checkedId()

            self.radio2_group = QButtonGroup(self)
            self.radio2_group.addButton(self.radioButton, id=7)
            self.radio2_group.addButton(self.radioButton_2, id=6)
            self.radio2_group.addButton(self.radioButton_3, id=5)
            self.radio2_group.addButton(self.radioButton_4, id=4)
            self.radio2_group.addButton(self.radioButton_5, id=3)
            check_quantidade=self.radio2_group.checkedId()



            # Número total de elementos no grupo
            n = int(check_quantidade)

            # Tamanho de cada combinação
            k = int(check_modo)

            # Calcular o número de combinações possíveis
            quantidade_combinacoes = math.comb(n, k)
            if int(check_modo) == 3:
                recebe=130/int(quantidade_combinacoes)
                self.lineEdit_5.setText(str(recebe))
            if int(check_modo)==4:
                recebe = 1300 / int(quantidade_combinacoes)
                self.lineEdit_5.setText(str(recebe))

            if len(bicho_provavel_temporario_set) > 2 and len(bicho_provavel_temporario_set) <= quantidade:

                # Imprimindo bichos para o proximo sorteio--------------------------------------------------
                self.lineEdit_4.setText(str(bicho_provavel_temporario_set))

            else:
                self.lineEdit_4.setText("Não possui jogos para os valores informados")
            cont += 1
        except:
            self.textEdit.setText("Precisa preencher corretamente os campos")
            cont += 1

def lista_milhares_jogos():
    """Cria uma lista com todos os jogos a onde cada item possui todas as milhares sorteadas"""
    lista=[]
    for data in dados:

        # Percorrendo todos os jogos ----------------------------------------------
        for datas, jogos in data.items():
            # Criando uma lista com todos os sorteios do jogo -------------------------
            for x in jogos:
                vv = []
                for b in x.values():
                    #Retirando o número º dos sorteios e espaço--------------------
                    b = re.sub(r"\d+º", "", b)
                    b = b.strip()
                    #Dividindo o numero para retirar a milhar
                    b = b.split("-")
                    if len(b)==2:
                     vv.append(b[0])
                lista.append(vv)


    return lista

def lista_grupos_jogos():
    """Cria uma lista com todos os jogos a onde cada item possui todas os grupos sorteadas"""
    lista=[]
    for data in dados:

        # Percorrendo todos os jogos ----------------------------------------------
        for datas, jogos in data.items():
            # Criando uma lista com todos os sorteios do jogo -------------------------
            for x in jogos:
                vv = []
                for b in x.values():
                    #Retirando o número º dos sorteios e espaço--------------------
                    b = re.sub(r"\d+-", "", b)
                    b = b.strip()
                    vv.append(b)
                lista.append(vv)


    return lista

def lista_grupos(*args):
   """Retorna uma lista tendo em cada item uma lista de grupos, 1 sorteio,2sorteio etc"""
   jogo1 = []
   jogo2 = []
   jogo3 = []
   jogo4 = []
   jogo5 = []
   for data  in dados:

    # Percorrendo todos os jogos ----------------------------------------------
     for datas, jogos in data.items():

        #percorrendo jogos que é uma lista de jogos, indo só nos jogos escolhidos
        lista=list(args)
        if len(lista)==0:
            lista=[0,1,2,3,4]
        try:
          for horario in lista:
            x=jogos[horario]
            jogo1.append(x['l-te 2'][-2:].strip("-"))
            jogo2.append(x['l-te 3'][-2:].strip("-"))
            jogo3.append(x['l-te 4'][-2:].strip("-"))
            jogo4.append( x['l-te 5'][-2:].strip("-"))
            jogo5.append( x['l-te 6'][-2:].strip("-"))

        except:
            ...
   return [jogo1,jogo2,jogo3,jogo4,jogo5]

def milhar_centena_cabeca_confere(lista):
 """Essa função retorna quantas milhares e centena de um sorteio anterior deram na cabea no próximo sorteio.
    no tributo devemos usar uma lista contendo listas com sorteios de jogos
 """

 recebe=lista()
 cont=1
 centena=0
 centena_dentro=0
 milhar=0
 milhar_dentro=0
 valor_gasto=0
 gasto=0
 tota=0


 #Colocando em jogos os 7 sorteios--------------
 for jogos in recebe:


    #Pegando cada milhar do jogos----------------------------------
    try:
       #Conferindo as milhares acertadas na cabeça----------------------------
       if recebe[cont][0] in jogos:
            print(jogos)
            print(recebe[cont][0])
            milhar+=1
            input("Milhar cabeça")

       #Conferindo as centenas acertadas na cabeça-------------------------------
       for milhares in jogos:
           if milhares[-3:]==recebe[cont][0][-3:]:
               centena += 1
               print(milhares[-3:])
               print(recebe[cont])
               input("Centena cabeça")


    except:
        cont += 1
        continue
    cont+=1

    #print(cont)
    if cont>=len(recebe):

        valor=cont-1
        valor_gasto=valor*3.5
        milhar=milhar*1000
        centena=centena*150
        print(f"valor gasto:R${valor_gasto}")
        print(f"premio milhar:R${milhar}")
        print(f"premio centena:R${centena}")

        break

def milhar_centena_dentro_conferir(lista):
    recebe = lista()
    cont = 1
    centena_dentro = 0
    milhar_dentro = 0
    valor_gasto = 0
    gasto = 0
    tota = 0
    for jogos in recebe:
      try:
        # Passando pelos jogos do dia e conferindo 1 a 1 com os jogos do dia futuro , aqui vale por dentro----------
        # Para milhar--------------------------
        for milhar_de_jogos in jogos:

            if milhar_de_jogos in recebe[cont]:
                milhar_dentro += 1
                print(milhar_de_jogos)
                print(recebe[cont])
                input("enter")

            # Para centena ------------------------
            # Retirando a centena da milhar-----------------
            recebendo_centena = []
            for centena_futuro in recebe[cont]:
                recebendo_centena.append(centena_futuro[-3:])

            if milhar_de_jogos[-3:] in recebendo_centena:
                centena_dentro += 1
                print(milhar_de_jogos[-3:])
                print(recebendo_centena)
                input("eneter")
      except:
          cont += 1
          continue
      cont += 1

      if cont >= len(recebe):
          valor = cont - 1
          valor_gasto = valor * 1.75
          centena_dentro = centena_dentro * 30
          milhar_dentro = milhar_dentro * 143
          print(valor_gasto)
          print(f"premio milhar_dentro:R${milhar_dentro}")
          print(f"premio centena_dentro:R${centena_dentro}")
          break

def jogos_novos():
   """Abre o arquivo json novo e cria uma lista de lista de jogos"""
   lista_principal=[]
   with open("bicho2.json","r") as arquivo:
       recebe=json.load(arquivo)

   #Abrindo cada sorteio_______________________
   for sorteio in recebe:

       #Eliminando os sorteios vazios e trabalhando com os que estão com valor____________________
       if not "" in list(sorteio.values()):

           #Retirar a milhar dos jogos para formar lista de jogos do sorteio ______________________________________
           lista_intermediaria=[]
           cont=1
           for milhar_centena in list(sorteio.values()):

                milhar_centena=re.sub(r"\d+º","", milhar_centena)
                milhar_centena=milhar_centena.strip()
                milhar_centena=milhar_centena[0:4]
                if cont==7:
                    milhar_centena=milhar_centena[0:3]
                lista_intermediaria.append(milhar_centena)
                cont+=1
           lista_principal.append(lista_intermediaria)

   return lista_principal




milhar_centena_cabeca_confere(jogos_novos)












