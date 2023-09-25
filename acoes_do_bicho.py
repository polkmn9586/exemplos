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
from criador import Criador
from ast import literal_eval
import re

class MainWindows(QMainWindow,Criador):

    def __init__(self,parent=None):
        super().__init__(parent)

        self.menu_init()
        self.menu_jogos_acumulados()
        self.menu_jogos_sorteados()
        self.menu_inserir_jogos()


        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def menu_init(self):
        self._arquivo = self._jogos  # Aqui estão todos os jogos
        self.lista_dos_dias=self._listar_dias_arquivo

        self._jogos_escolhidos = []  # Aqui a lista dos jogos do sorteio
        self._jogos_escolhidos_por_dia = []  # Aqui a lista dos jogos
                                             # acumulados dos dias escolhidos sem a data
        self._jogos_escolhidos_por_dia_data = [] # Aqui a lista dos jogos
                                                 # acumulados dos dias escolhidos com a data
        self.dicionario_dezenas_mais_dadas = {}# possui as dezenas e quantidade de vezes que foi dada
        self.lista_bichos_data=[]#lista com os grupos sorteados de acordo com a data determinada
        self.dicionario_bicho_atraso = {}# dicionário com o bicho e o atraso
        self.bichos_tempo_espera={}# Dicionário com bicho e lista do tempo que demorou para sair
        self.bicho_provavel=[]# lista de bichos provaveis de serem sorteados

        self.bicho_aposta = {}

        self._lista_grupos = []


        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Jogo do Bicho")
        self.center_widget = QWidget()
        self.setCentralWidget(self.center_widget)
        self.layout = QGridLayout()
        self.center_widget.setLayout(self.layout)
    def menu_jogos_acumulados(self):

            self.data_label_excluidos = QLabel("Escolha os jogos para excluir: ")
            self.data_label_excluidos.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.data_label_inicio=QLabel("Data Inicial")
            self.data_label_final=QLabel("Data Final")
            self.data_tex_excluido11 = self.criar_checkBox(self.layout, "11",2,4)
            self.data_tex_excluido14 = self.criar_checkBox(self.layout, "14", 2, 5)
            self.data_tex_excluido16 = self.criar_checkBox(self.layout, "16", 2, 6)
            self.data_tex_excluido19 = self.criar_checkBox(self.layout, "19", 2, 7)
            self.data_tex_excluido21 = self.criar_checkBox(self.layout, "21", 2, 8)

            self.data_combo_inicio=self.criar_comboBox(self.layout,self.lista_dos_dias,2,1)
            self.data_combo_final =self.criar_comboBox(self.layout,self.lista_dos_dias,2,2)


            self.botao2 = QPushButton("Grupos com mais saída")
            self.botao2.clicked.connect(self.grupos_mais_dados_acumulado)
            self.gerador_grupos=self.criar_Pushbutton(self.layout,"Gerar grupos para o proximo sorteio",11,2,self._prejuizo_ganho_grupo)
            self.combo_gerador_grupos=self.criar_comboBox(self.layout,[],12,2,1,1)
            self.label_relatorio=self.criar_label(self.layout,f"Relatório de ganhos usando as datas \nescolhidas "
                                                              f"e os grupos com possibilidade\n para o próximo sorteio ",13,2,1,2)
            self.tline_relatorio=self.criar_text_edit(self.layout,"",14,2,1,1)
            self.criar_Pushbutton(self.layout,"Grupos com mais saída",11,1,self.grupos_mais_dados_acumulado)
            self.dezenas_mais_dadas = self.criar_comboBox(self.layout, [], 12, 1, 1, 1)
            self.valor=None




            self.layout.addWidget(self.data_label_excluidos, 2, 3)
            self.layout.addWidget(self.data_label_final, 1, 2)
            self.layout.addWidget(self.data_label_inicio, 1, 1)


    def menu_jogos_sorteados(self):

            self.label_espaco_amigos=self.criar_label(self.layout,x=14,y=1,l=1,c=3)
            self.label_apresentacao_amigos = self.criar_label(self.layout,"------------------ Jogo dos amigos -------------------------",15,1,1,3)
            self.label_data_amigos = self.criar_label(self.layout, "Digite a data inicial do sorteio:",17, 1,1,1)
            self.line_data_amigos=self.criar_line(self.layout,17,2,1,1)
            self.label_grupos_amigos = self.criar_label(self.layout, "Grupos sugeridos:",18, 1,1,1)
            self.label_grupos_sugeridos_amigos = self.criar_label(self.layout, " #-#-#-#-#-#-#-#-#-#", 18, 2,1,1)
            self.push_enviar_amigos=self.criar_Pushbutton(self.layout,"Enviar dados",19,1,self._acumulo_de_jogos_amigos)

    def menu_inserir_jogos(self):
        self.criar_label(self.layout,"------------------ Inserir jogos -------------------------",11,3,1,3)
        self.ultimadata_label_criaJogos=self.criar_label(self.layout, f"     Data do ultimo jogo inserido: {self.ultima_data_arquivo} ", 12, 3, 1, 1)
        self.criar_label(self.layout,  "\tCopiar próximo  jogo aqui", 13, 3, 1, 3)
        self.receber_jogo=self.criar_text_edit(self.layout,"",14,3,1,2)
        self.enviar_jogos=self.criar_Pushbutton(self.layout,"Eviar jogos",15,3,self.adicionar_jogos)




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

        for x in self._arquivo[0].keys():
            ...
        return x

    @property
    def ultima_data_arquivo(self):

        for x in self._arquivo[-1].keys():
          ...
        return x



    def _acumulo_de_jogos_amigos(self):
        print("_acumulo_de_jogos_amigos")
        self._jogos_escolhidos_por_dia=[]
        data_final_arquivo=self.ultima_data_arquivo
        data_final_arquivo=datetime.strptime(data_final_arquivo,"%d/%m/%Y") # pegando a ultima data do
                                                                            # arquivo para conferência

        data_final=self.line_data_amigos.text() #data_final recebe data final em str
        data_final=datetime.strptime(data_final,"%d/%m/%Y")# faremos a conversão da str
                                                     # em data, colocando em data_final
        if data_final_arquivo < data_final: # Lógica criada para pegar o último dia no
                                            # caso de uma data maior
            data_final=data_final_arquivo

        data=data_final-timedelta(days=9) # agora como data , tiramos 5 dias
        data=data.strftime("%d/%m/%Y") # retransformamos em str
        data_final = data_final-timedelta(days=1) # retirando 1 dia da data escolhida do sorteio
        data_final=data_final.strftime("%d/%m/%Y")# retransformamos em str

        lista_coonvertida_jogos_excluidos = [3,4] # jogos excluídos

        lista_de_jogos = self._arquivo  # Carregando todos os jogos

        chave_saida="" # chave usada para sair da repetição
        chave_de_entrada=0 # chave usada para alterar o valor da data

        for numeracao_do_item, item_lista in enumerate(lista_de_jogos):  # Vou acessar cada ítem da lista
                                                                         # que é uma biblioteca
            if chave_saida=="ok":
                break
            for chave_do_item in item_lista.keys():  # Explorando cada  chave dos itens da lista
                                                     #  procurando a data
                if chave_saida == "ok":
                  break


                if chave_de_entrada==1:# Caso já tenha acessado a primeira data esse elemento será
                                      # modificado para 1 e data mudará o seu valor
                     data=chave_do_item



                if chave_do_item == data:  # Aqui quando achamos a data desejado, começo da lógica

                    chave_de_entrada=1

                    for ordenacao_itens_dia, itens_do_dia in enumerate(lista_de_jogos[numeracao_do_item][chave_do_item]):  # Aqui vamos coletar os jogos

                        if ordenacao_itens_dia in lista_coonvertida_jogos_excluidos:  # Lógica para pular se for o jogo escolhido

                            continue


                        self._jogos_escolhidos_por_dia.append(itens_do_dia)  # jogo adicionado


                    if chave_do_item == data_final:  # Aqui se for = a data de termino finaliza tudo
                        chave_saida = "ok"
                        grupos_mais_dados_2=[]
                        grupos_mais_dados_2_ran=[]
                        grupos_mais_dados=self._dicionario_dezenas_mais_dados(self._jogos_escolhidos_por_dia)
                        for chave , valor in grupos_mais_dados.items():
                            if valor == 2:
                                chave=int(chave)
                                grupos_mais_dados_2.append(chave)



                        grupos_mais_dados_2_ran=sample(grupos_mais_dados_2,10)
                        self.label_grupos_sugeridos_amigos.setText(str(grupos_mais_dados_2_ran))

                        break

    def _dicionario_dezenas_mais_dados(self, lista):
        """ Cria um dicionário de dezenas com sua quantidade de vezes
        sortiada, suprindo self.dicionario_dezenas_mais_dadas"""
        print("_grupos_mais_dados")
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
        self.data_inicial = self.data_combo_inicio.currentText()
        self.data_final =self.data_combo_final.currentText()
        self._acumulo_de_jogos()

    def _acumulo_de_jogos(self, *args):
        """Gera uma lista de dicionário com os jogos sem data dos dias escolhidos ,
            retornando a mesma e suprindo self._jogos_escolhidos_por_dia"""
        print("_acumulo_de_jogos")
        self._jogos_escolhidos_por_dia = []
        self._jogos_escolhidos_por_dia_data = []
        data = self.data_combo_inicio.currentText()  # Pegando data inicial
        data_final = self.data_combo_final.currentText()  # Pegando data final

        sorteio = {11: 0, 14: 1, 16: 2, 19: 3, 21: 4}  # Usaremos  para  escolher as partidas
        # do  jogo que iremos cortar

        lista_coonvertida_jogos_excluidos = []  # criando uma lista com o que não vai ser usado
        if self.data_tex_excluido11.isChecked():
            lista_coonvertida_jogos_excluidos.append(0)
        if self.data_tex_excluido14.isChecked():
            lista_coonvertida_jogos_excluidos.append(1)
        if self.data_tex_excluido16.isChecked():
            lista_coonvertida_jogos_excluidos.append(2)
        if self.data_tex_excluido19.isChecked():
            lista_coonvertida_jogos_excluidos.append(3)
        if self.data_tex_excluido21.isChecked():
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
                        print(self._jogos_escolhidos_por_dia)
                        return self._jogos_escolhidos_por_dia

                        break

    def adicionar_jogos(self):
          print("adicionar_jogos")
          try:
            lista=literal_eval(self.receber_jogo.toPlainText())# Convertendo str em lista

            if isinstance(lista, list) and lista !="": # verificando se está vazia ou se é uma lista
                self.ultimadata_label_criaJogos.setText(f"   Data do ultimo jogo inserido: {self.ultima_data_arquivo} ")
                self.receber_jogo.setText("Lista enviada")
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

            else:
                self.receber_jogo.setText("A entrada não é uma lista válida.")
          except:
                self.receber_jogo.setText("A entrada não é uma lista válida.")
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
       self.dezenas_mais_dadas.clear()
       recebe=[]
       for x,y in  valor.items():
           recebe.append(f"{x}={y}, ")


       self.dezenas_mais_dadas.addItems(recebe)


       self._jogos_escolhidos_por_dia=[]


    def _criar_dicionario_tempos_de_espera(self):
        """Cria um dicionário com o número do bicho ligado a uma lista
           de tempos que demorou para ser sorteado"""

        print("_criar_dicionario_tempos_de_espera")
        dicionario_tempos = {}  # Um dicionário para armazenar as contagens de tempos
        self.bichos_tempo_espera={}

        for i in range(len(self.lista_bichos_data)):
            item = self.lista_bichos_data[i]  # Item da lista em questão
            if item not in dicionario_tempos:
                dicionario_tempos[item] = []  # Inicializa uma lista vazia para o item

            if item in self.lista_bichos_data[i + 1:]:  # Aqui é feita uma pergunta se ele aparecerá nos próximos
                # itens , caso não apareça fica com o último valor
                indice_proxima_ocorrencia = self.lista_bichos_data.index(item, i + 1)  # aqui quando ele irá aparecer
                # , apartir de uma casa na frente para não pegar
                # a sua posição e sim a da próxima repetição
                tempo_demora = indice_proxima_ocorrencia - i  # diminuo a posição atual do lugar aonde se encontra o próximo
                dicionario_tempos[item].append(tempo_demora)  # adicionando

        for bicho , tempo_lista in dicionario_tempos.items():
            if tempo_lista!=[]:
                self.bichos_tempo_espera[bicho]=tempo_lista
        #self.bichos_tempo_espera=dicionario_tempos
        print(self.bichos_tempo_espera)
        self._bicho_atrasado()

    def _lista_de_bichos(self):
        """Cria uma lista com os números dos grupos sortiados dos jogos escolhidos por data"""
        print("_lista_de_bichos")
        resultado = []

        for dicionario in self._jogos_escolhidos_por_dia_data:
            for data, valores in dicionario.items():
                for valor in valores:
                    l_te_2 = valor.get("l-te 2", "")
                    # Usando regex para encontrar os dois últimos números após o hífen
                    numeros = re.findall(r'-(\d+)$', l_te_2)
                    if numeros:
                        resultado.append(int(numeros[0]))

        self.lista_bichos_data=resultado
        self._criar_dicionario_tempos_de_espera()
    def _bicho_atrasado(self):
        dicionario_bicho_atraso = {}
        contador = 0
        for bichos, repeti in self.bichos_tempo_espera.items():

            if repeti != []:
                contador+=1
                self.dicionario_bicho_atraso[bichos]=self.lista_bichos_data[::-1].index(bichos)

            if contador==0:
                print("nada")
        self._cria_lista_de_grupos_provaveis()

    def _cria_lista_de_grupos_provaveis(self):
        self.combo_gerador_grupos.clear()
        self.bicho_provavel=[]


        for bicho, atraso in self.dicionario_bicho_atraso.items():
            if atraso>29 and atraso<48:

                self.bicho_provavel.append(f"Jogar o grupo :{bicho} Atrasado : {atraso}")

        print(self.bicho_provavel)
        self.combo_gerador_grupos.addItems(self.bicho_provavel)


    def _prejuizo_ganho_grupo(self):
        print("self._prejuizo_ganho_grupo")
        self.tline_relatorio.clear()
        self._d_inicial_final()
        self._lista_de_bichos()
        # criar uma dic prejuizo do bicho
        # criar uma dic ganho do bicho
        # criar um elemento acumulador do ganho para colocar no valor ganho bicho
        # criar um elemento aumulador da perda para colocar no valor prejuizo bicho
        #criar um elemento aumulador das  perdas para diminuir do ganho
        # criar um elemento aumulador dos  ganhos para ser subtraido da perda
        self.prejuizo_grupo={}
        self.ganho_grupo={}
        ganho_bicho=0
        prejuizo_bicho=0
        acumulo_ganho=0
        acumulo_perda=0
        #preciso passar por todos os resultados do bicho tempo_espera
        for bicho , acertos in self.bichos_tempo_espera.items():
        #preciso acessar cada elemento do seu value
           for item in acertos:
        #saber se é maior que 28 e menor que 48 e se é maior ou igual que 48
              if item >=29 and  item<48:
        # se maior que 28 pego esse valor diminuo de 48 e acrescento no value do ganho do bicho
                 ganho_bicho+=48 - item
                 self.ganho_grupo[bicho]=ganho_bicho
                 acumulo_ganho+=ganho_bicho
              if item>=48:
        # se maior ou igual a 48 pego esse bicho e acrecento 18 reais no value dic prejuizo do bicho
                  prejuizo_bicho+=18
                  self.prejuizo_grupo[bicho]=prejuizo_bicho
                  acumulo_perda+=prejuizo_bicho
              ganho_bicho=0
              prejuizo_bicho=0
        # essas variaveis precisam ser sempre zeradas pos precisam trazer o valor atual de acordo com a data em escolha
        print(self.bicho_provavel)
        self.tline_relatorio.setText(f"Ganho:{acumulo_ganho} Perda: {acumulo_perda} = {acumulo_ganho - acumulo_perda} Ganhos" )
        print(f"Seu ganho foi de: {self.ganho_grupo}\nSua perda de: {self.prejuizo_grupo}")
app=QApplication(sys.argv)
window=MainWindows()
window.show()
app.exec()







