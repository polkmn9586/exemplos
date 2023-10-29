from itertools import groupby
import json
from datetime import datetime,timedelta
from datetime import datetime
from dateutil import relativedelta
import sys
from PySide6.QtCore import Slot,Qt
from random import randint, sample
from PySide6.QtWidgets import QApplication,QMainWindow, QWidget,QGridLayout,QPushButton,QLineEdit,QLabel,QTextEdit,QCheckBox,QComboBox
import sys

from ast import literal_eval
import re
from programa_do_bicho2 import Ui_Form
from criador import Criador
from PySide6.QtGui import QIcon
from exemplo1 import   treino_grupos_sorteados_juntos, bicho,grupos_provaveis
from pathlib import Path

class Dicionario():
    def __init__(self,dicionario:dict,*args,**kwargs):

        self.dicionario=None



    @property
    def lista(self):

        recebe=self.dicionario.keys()
        recebe=list(recebe)
        return recebe

    def numeros(self,lista):
        recebe=self.dicionario[lista].keys()
        return recebe
    def repeticao(self,lista,numero):
        recebe = self.dicionario[lista]

        recebe = recebe[numero]
        return recebe
    #@property



class MainWindows(QWidget,Ui_Form,Dicionario):

   def __init__(self):
        super(MainWindows,self).__init__()

        self.setupUi(self)

        self.menu_init()
        self.menu_jogos_acumulados()

        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
        self.menu_inserir_jogos()
        self.menu_estatistica_terno_e_4_de_grupo()

   def menu_init(self):

        self._arquivo = self._jogos  # Aqui estão todos os jogos
        self.lista_dos_dias=self._listar_dias_arquivo

        self._jogos_escolhidos = []  # Aqui a lista dos jogos do sorteio
        self._jogos_escolhidos_por_dia = []  # Aqui a lista dos jogos
                                             # acumulados dos dias escolhidos sem a data
        self._jogos_escolhidos_por_dia_data = [] # Aqui a lista dos jogos
                                                 # acumulados dos dias escolhidos com a data
        self.dicionario_dezenas_mais_dadas = {}# possui as dezenas e quantidade de vezes que foi dada


        self.lista_bichos_data=[]      #lista com os grupos sorteados de acordo com a data determinada
        self.lista_bichos_data2 = []
        self.lista_bichos_data3 = []
        self.lista_bichos_data4 = []
        self.lista_bichos_data5 = []
        self.lista_bicho_5sorteios=[]#Criar uma lista com 5 listas de grupos sorteados , criado : _lista_de_bichos1


        self.dicionario_bicho_atraso = {}# dicionário com o bicho e o atraso
        self.bichos_tempo_espera={}# Dicionário com bicho e lista do tempo que demorou para sair
        self.bicho_provavel=[]# lista de bichos provaveis de serem sorteados
        self.relacao_grupos_provaveis={} # biblioteca que gera um dic dos possíveis grupos em cada sorteio para jogar
        self.grupos_provaveis_preparados={} #objeto que permite extrair elementos do dic self.relacao_grupos_provaveis
        self.bicho_aposta = {}

        self._lista_grupos = []
        self.menor=25
        self.maior=30

   def menu_jogos_acumulados(self):


            self.comb_inicio.addItems(self.lista_dos_dias)
            self.comb_final.addItems(self.lista_dos_dias)

            self.push_g_mais.clicked.connect(self.grupos_mais_dados_acumulado)
            self.push_g_sorteio.clicked.connect(self._lista_de_bichos1)

            self.valor=None

   def menu_inserir_jogos(self):



        self.line_ins_jogos.setText("1")
        #self.enviar_jogos=self.push_ins_jogos
        self.push_ins_jogos.clicked.connect(self.adicionar_jogos)

   def menu_terno_e_4_de_grupo(self):
       self.push_g_sorteio.clicked.connect(self._lista_de_bichos1)

   def menu_estatistica_terno_e_4_de_grupo(self):
       self.pushButton.clicked.connect(self._lista_de_bichos1)


   @property
   def _jogos(self):
        "Retorna a lista de todos os jogos que estão no arquivo"
        with open("bicho.json","r") as arquivo:
           dados=json.load(arquivo)
           return dados
   @property
   def _listar_dias_arquivo(self):
        "Retorna uma lista dos dias do arquivo em str"
        print("_listar_dias_arquivo")
        lista_dos_dias=[]
        for itens in self._arquivo:

            for key, valu in itens.items():
              lista_dos_dias.append(key)
        return lista_dos_dias
   @property
   def primeira_data_arquivo(self):
        print("primeira_data_arquivo")

        for x in self._arquivo[0].keys():
            ...
        return x

   @property
   def ultima_data_arquivo(self):
        print("ultima_data_arquivo")

        for x in self._arquivo[-1].keys():
          ...
        return x

   def _dicionario_dezenas_mais_dados(self, lista):
        """ Cria um dicionário de dezenas com sua quantidade de vezes
        sortiada, suprindo self.dicionario_dezenas_mais_dadas"""
        print("_dicionario_dezenas_mais_dados")
        lista_agrupamento = {}
        self._lista_grupos = []
        for itens in lista:
            self._lista_grupos.append(itens['l-te 2'][5:7])
            self._lista_grupos.append(itens['l-te 3'][5:7])
            self._lista_grupos.append(itens['l-te 4'][5:7])
            self._lista_grupos.append(itens['l-te 5'][5:7])
            self._lista_grupos.append(itens['l-te 6'][5:7])
            self._lista_grupos.append(itens['l-te 7'][5:7])

        lista_ordenada = sorted(self._lista_grupos)
        agrupamento = groupby(lista_ordenada)

        for x, y in agrupamento:
            lista_agrupamento[x] = len(list(y))
            agrupamento_ordenado = dict(sorted(lista_agrupamento.items(), key=lambda item: item[1], reverse=True))
        self.dicionario_dezenas_mais_dadas=agrupamento_ordenado
        return agrupamento_ordenado

   def _d_inicial_final(self):
        print("_d_inicial_final")
        self.data_inicial = self.comb_inicio.currentText()
        self.data_final =self.comb_final.currentText()
        self._acumulo_de_jogos()



   def adicionar_jogos(self):
          print("adicionar_jogos")
          try:
            lista=literal_eval(self.line_ins_jogos.text())# Convertendo str em lista

            if isinstance(lista, list) and lista !="": # verificando se está vazia ou se é uma lista
                self.line_ins_jogos.setText("Lista enviada")
                lista_nova = []  # recebo a lista só com os jogos
                for x, y in enumerate(lista):  # lógica da lista correta
                    if x % 2 == 1:
                        lista_nova.append(y)

                with open("bicho.json", "r") as arquivo:  # Abrindo o arquivo
                    dados = json.load(arquivo)

                for dia in dados[-1].keys():
                    ultima_data = dia
                formato = "%d/%m/%Y"
                data = datetime.strptime(ultima_data, formato)  # criando uma data
                data = data + timedelta(days=1)  # Adicionando um dia a data
                data = data.strftime("%d/%m/%Y")  # entregando uma string da data

                dados.append({data: lista_nova})
                texto = json.dumps(dados, ensure_ascii=False, indent=2)
                with open("bicho.json", "w") as arquivo:
                    arquivo.write(texto)
                self._d_inicial_final()
            else:
                self.line_ins_jogos.setText("A entrada não é uma lista válida.")
          except:
                self.line_ins_jogos.setText("A entrada não é uma lista válida.")
   def dias_dos_sorteios(self, data=None, jogo=None, quantidade=1000):
     """lista de dicionários de jogos escolhidos"""
     print("dias_dos_sorteios")
     jogos_escolhidos = [] # Lista dos jogos selecionados
     sorteio={11:0,14:1,16:2,19:3,21:4}
     lista_coonvertida_jogos_excluidos=[4,3]

     lista_de_jogos = self._arquivo # Carregando todos os jogos


     for numeracao_do_item, item_lista in enumerate(lista_de_jogos): # Vou acessar cada ítem da lista
                                                                     # que é uma biblioteca
        for chave_do_item in item_lista.keys(): # Explorando cada chave da
                                                # biblioteca a procurando da data

           if chave_do_item == data: # Aqui quando achamos a data desejado, começo da lógica
             contador=1 # irá contar quantos jogos serão gerados

             for ordenacao_itens_dia, itens_do_dia in enumerate(lista_de_jogos[numeracao_do_item][chave_do_item][sorteio[jogo]:]): # Aqui vamos coletar os jogos do 1
                                                                       # dia escolhido a partir do jogo escolhido

               if ordenacao_itens_dia in lista_coonvertida_jogos_excluidos: # Lógica para pular se for o jogo escolhido

                  continue


               self._jogos_escolhidos.append(itens_do_dia) # jogo adicionado

               contador+=1


               if contador > quantidade: # Aqui se for o caso vamos para os jogos posteriores ou vamos sair
                 return self._jogos_escolhidos
                 break



             sair="" # Usamos para sair das repetições a baixo



             while True:

                  if sair=="ok": # Chave para sair da repetição
                    break

                  try:
                     numeracao_do_item+=1 # Aqui vamos para o próximo ítem ate alcançar a quantidade de jogos
                     posicao=0

                     for itens_posteriores in lista_de_jogos[numeracao_do_item].values(): # Pegaremos aqui o conjunto de ítens posteriores
                        if sair == "ok":  # Chave para sair da repetição
                          break
                        ordenacao_itens_dia = 0  # zerando a posição dos jogos
                        for item_dos_posteriores in itens_posteriores:  # Pegaremos aqui itens do conjunto dos itens posteriores


                           if ordenacao_itens_dia in lista_coonvertida_jogos_excluidos:  # Lógica para pular se for o jogo escolhido
                              posicao+=1

                              ordenacao_itens_dia+=1
                              continue

                           self._jogos_escolhidos.append(item_dos_posteriores)  # jogo adicionado
                           contador += 1
                           posicao+=1
                           if contador > quantidade:  # Aqui se for o caso vamos para os jogos posteriores ou vamos sair
                              sair = "ok"
                              return self._jogos_escolhidos
                              break

                  except:
                   return self._jogos_escolhidos
                   break
             return self._jogos_escolhidos

   def grupos_mais_dados_acumulado(self):
       print("grupos_mais_dados_acumulado")
       valor=self._dicionario_dezenas_mais_dados(self._acumulo_de_jogos())# cria um dicionário com dezenas e
                                                                         # quantidade de vezes dada
       self.combo_g_mais.clear()
       recebe=[]
       for x,y in  valor.items():
           recebe.append(f"{x}={y}, ")


       self.combo_g_mais.addItems(recebe)


       self._jogos_escolhidos_por_dia=[]


   def _acumulo_de_jogos(self, *args):
        """Gera uma lista de dicionário com os jogos sem data dos dias escolhidos ,
            retornando a mesma e suprindo self._jogos_escolhidos_por_dia"""
        print("_acumulo_de_jogos")
        self._jogos_escolhidos_por_dia = []
        self._jogos_escolhidos_por_dia_data = []
        data = self.comb_inicio.currentText()  # Pegando data inicial
        data_final = self.comb_final.currentText()  # Pegando data final

        sorteio = {11: 0, 14: 1, 16: 2, 19: 3, 21: 4}  # Usaremos  para  escolher as partidas
        # do  jogo que iremos cortar

        lista_coonvertida_jogos_excluidos = []  # criando uma lista com o que não vai ser usado
        if self.check_11.isChecked():
            lista_coonvertida_jogos_excluidos.append(0)
        if self.check_14.isChecked():
            lista_coonvertida_jogos_excluidos.append(1)
        if self.check_16.isChecked():
            lista_coonvertida_jogos_excluidos.append(2)
        if self.check_19.isChecked():
            lista_coonvertida_jogos_excluidos.append(3)
        if self.check_21.isChecked():
            lista_coonvertida_jogos_excluidos.append(4)

        lista_de_jogos = self._arquivo  # Carregando todos os jogos

        chave_saida = ""  # chave usada para sair da repetição
        chave_de_entrada = 0  # chave usada para alterar o valor da data

        for numeracao_do_item, item_lista in enumerate(lista_de_jogos):  # Vou acessar cada ítem da lista
            # que é uma biblioteca
            if chave_saida == "ok":
                break
            for chave_do_item in item_lista.keys():  # Explorando cada  chave dos itens da lista
                #  procurando a data
                if chave_saida == "ok":
                    break

                if chave_de_entrada == 1:  # Caso já tenha acessado a primeira data esse elemento será
                    # modificado para 1 e data mudará o seu valor

                    data = chave_do_item  # Aqui data se modifica recebendo o valor da data corrente

                if chave_do_item == data:  # Aqui quando achamos a data desejado, começo da lógica

                    chave_de_entrada = 1
                    recebe = []
                    for ordenacao_itens_dia, itens_do_dia in enumerate(
                            lista_de_jogos[numeracao_do_item][chave_do_item]):  # Aqui vamos coletar os jogos

                        if ordenacao_itens_dia in lista_coonvertida_jogos_excluidos:  # Lógica para pular se for o jogo escolhido

                            continue

                        recebe.append(itens_do_dia)
                        self._jogos_escolhidos_por_dia.append(itens_do_dia)  # jogo adicionado

                    self._jogos_escolhidos_por_dia_data.append({chave_do_item: recebe})

                    if chave_do_item == data_final:  # Aqui se for = a data de termino finaliza tudo
                        chave_saida = "ok"
                        print(f"vamos:{self._jogos_escolhidos_por_dia_data}")
                        return self._jogos_escolhidos_por_dia

                        break

   def _lista_de_bichos1(self):
       """Cria uma lista com os números dos grupos sortiados dos jogos escolhidos por data, primeiro passo para achar os
           grupos ideais para serem jogados, criando 5 listas em variaveis referentes ao sorteio"""
       print("_lista_de_bichos1")
       self._d_inicial_final()

       # for cc in self._jogos_escolhidos_por_dia_data: # Texte printa todos os jogos com data e jogos
       # print(cc)


       resultado = []

       escolhas_jogos = {0: "l-te 2", 1: "l-te 3", 2: "l-te 4", 3: "l-te 5",
                         4: "l-te 6"}  # aqui  opções para escolha de jogos
       escolhas_jogos_arma = {0: self.lista_bichos_data, 1: self.lista_bichos_data2, 2: self.lista_bichos_data3,
                              3: self.lista_bichos_data4,
                              4: self.lista_bichos_data5}  # aqui  opções para escolha de variaveis para

       # armazenar a lista dos bichos
       #Vamos percorrer os 5 sorteios como cabeçalho e para cada sorteio vamos percorrer um dic com data e jogos
       # e fazer operações

       for x in range(
               5):  # correrrá 5 posições para usar x para biblioteca das escolhas acima, mudando assim para criar 5 listas
           # , esse for irá nos levar para a construção da próxima lista com o novo prémio

           resultado = []  # zerando resultado para próxima lista de grupos

           # Mais um for que sera um cabeçalho iremos correr todas as datas
           for dicionario in self._jogos_escolhidos_por_dia_data:  # chama um dicionário composto por uma data e uma lista de jogos
               # , irá percorrer data por data, esse for fechará a data para o sorteio

               #
               for data, jogos in dicionario.items():  # irá percorrer as listas do dia em destaque, em média 4 jogos
                   for valor in jogos:  # valor é um jogo, uma bibliotéca com os prémios
                       l_te_2 = valor.get(escolhas_jogos[x], "")
                       # Usando regex para encontrar os dois últimos números após o hífen
                       numeros = re.findall(r'-(\d+)$', l_te_2)  # armazenando o grupo
                       if numeros:
                           resultado.append(
                               int(numeros[0]))  # salvando o grupo em resultados , lebrando que ele só ira servir
                           # para cada lista de bicho tendo que ser apagado ao iniciar uma nova

               escolhas_jogos_arma[x] = resultado # aqui colocamos em cada posição do 0 ao 5 uma  lista obtendo 5
                                                  # listas, que correspondem ao 5 sorteios

           lista=[] #vamos juntar as 5 listas aqui para criar o tempo de espera
           for itens,listas in escolhas_jogos_arma.items():#colocando com for a list em lista
            lista.append(listas)

       # essa função nos retorna 5 listas dentro de um dicionário
       # com os grupos possibilidade de sorteio
       self.lista_bicho_5sorteios=lista
       self.self_sender=self.sender()
       if self.self_sender==self.pushButton:
          treino_grupos_sorteados_juntos(self,self.lista_bicho_5sorteios,self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text())
       if self.self_sender == self.push_g_sorteio:

           grupos_provaveis(self, self.lista_bicho_5sorteios, self.lineEdit_6.text(),
                                          self.lineEdit_7.text(), self.lineEdit_8.text())


       #self._criar_dicionario_tempos_de_espera()
       #self.randon_provaveis()  # chamando esse metodo para colocar os elementos da lista dos jogos
       # escolhidos nos lugares do sorteio

   def randon_provaveis(self):
        print("randon_provaveis")
        self.dicionario = self.bicho_provavel #carrega em dicionario os grupos de 0 a 4 que serão usados

        #print(f"vamos  {self.dicionario}") # Imprimi o self dicionário
        #print(self.numeros(0))# imprimi um texte de um grupo


        if len(self.bicho_provavel[0])>=1:
            recebe=list(map(str,self.numeros(0)))
            #print(recebe)
            self.combo_g_sorteio.clear()
            self.combo_g_sorteio.addItems(sample(recebe,1))
        else:
            self.combo_g_sorteio.clear()
            self.combo_g_sorteio.addItems(["Sem Grupo"])



        if len(self.bicho_provavel[1])>=1:
            recebe = list(map(str, self.numeros(1)))
            # print(recebe)
            self.combo_g_sorteio_2.clear()
            self.combo_g_sorteio_2.addItems(sample(recebe,1))
        else:
            self.combo_g_sorteio_2.clear()
            self.combo_g_sorteio_2.addItems(["vazio"])

        if len(self.bicho_provavel[2])>=1:
            recebe = list(map(str, self.numeros(2)))
            # print(recebe)
            self.combo_g_sorteio_3.clear()
            self.combo_g_sorteio_3.addItems(sample(recebe,1))
        else:
            self.combo_g_sorteio_3.clear()
            self.combo_g_sorteio_3.addItems(["vazio"])

        if len(self.bicho_provavel[3]) >= 1:
            recebe = list(map(str, self.numeros(3)))
            # print(recebe)
            self.combo_g_sorteio_4.clear()
            self.combo_g_sorteio_4.addItems(sample(recebe, 1))
        else:
            self.combo_g_sorteio_4.clear()
            self.combo_g_sorteio_4.addItems(["vazio"])

        if len(self.bicho_provavel[4]) >= 1:
            recebe = list(map(str, self.numeros(4)))
            # print(recebe)
            self.combo_g_sorteio_5.clear()
            self.combo_g_sorteio_5.addItems(sample(recebe, 1))
        else:
            self.combo_g_sorteio_5.clear()
            self.combo_g_sorteio_5.addItems(["vazio"])

   def _criar_dicionario_tempos_de_espera(self):
        """Cria um dicionário com o número dos bichos podendo ser ligado a uma lista
           de tempos que demorou para ser sorteado"""
        print("_criar_dicionario_tempos_de_espera")


        self.bichos_tempo_espera={} # Armazenará a resposta final

        cont=0
        for listas in self.lista_bicho_5sorteios:# Vai andar os 5 sorteios que possuen uma lista com os bichos
          dicionario_tempos = {}  # Um dicionário para armazenar as contagens , se apagará a cada sorteio
          cont+=1
          #For que vai trabalhar com a lógica de cada item das lista
          for i in range(len(listas)):


#--------------------------lógica1 - -----------------------------------------------------------------------------------

            item = listas[i]  # Item da lista em questão
            if item not in dicionario_tempos:
                dicionario_tempos[item] = []  # Inicializa uma lista vazia para o item

            if item in listas[i + 1:]:  # Aqui é feita uma pergunta se ele aparecerá nos próximos
                                                        # itens , caso não apareça fica com o último valor

                indice_proxima_ocorrencia = listas.index(item, i + 1)  # aqui quando ele irá aparecer
                # , apartir de uma casa na frente para não pegar
                # a sua posição e sim a da próxima repetição


#---------------------------Resposta da lógica---------------------------------------------------------------
                tempo_demora = indice_proxima_ocorrencia - i  # diminuo a posição atual do lugar aonde se encontra o próximo
                dicionario_tempos[item]=(tempo_demora)  # Vai criando o dicionário com grupo e atraso

# ---------------------------Resposta final---------------------------------------------------------------
          if  self.bichos_tempo_espera:
             self.bichos_tempo_espera.update({cont:dicionario_tempos})

          else:
              self.bichos_tempo_espera={cont:dicionario_tempos}
          """for x, i in self.bichos_tempo_espera:"""


        self._bicho_atrasado()

   def _bicho_atrasado(self):
        print("_bicho_atrasado")

        contador = 0

        #esse é o for cabeça referente as listas
        for lista , valores in self.bichos_tempo_espera.items():

            dicionario_bicho_atraso = {}
            #for do dic que traz o grupo e seu atraso
            for bichos, repeti in valores.items():
                if repeti==[]:
                    repeti=0

  #------------------------- lógica-------------------------------------------------------------------
                if repeti >=self.menor and repeti <=self.maior:
                    if dicionario_bicho_atraso:
                      dicionario_bicho_atraso.update({bichos:repeti})
                    else:
                        dicionario_bicho_atraso={bichos:repeti}

 # ------------------------- Resposta final-------------------------------------------------------------------
            if self.bicho_provavel:
                 self.bicho_provavel.update({contador:dicionario_bicho_atraso})
                 contador += 1
            else:
                    self.bicho_provavel={contador: dicionario_bicho_atraso}
                    contador+=1




app=QApplication(sys.argv)
windows=MainWindows()


windows.show()
app.exec()



