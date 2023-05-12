import sys
from PySide6.QtWidgets  import QApplication,QWidget,QGridLayout,\
     QPushButton,QVBoxLayout,QTextEdit,QLabel,QMainWindow,QHBoxLayout
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
#--------------------------------------------criação  dos elementos com configuração---------------------
        self.janela=QWidget() # janela criada

        self.lay=  QVBoxLayout() # lay principal criado
        self.tamanho_lay(self.lay)# conf do lay principal

        self.lay1 = QHBoxLayout() # repetição da configuração dos lay com criação
        self.tamanho_lay(self.lay1)

        self.lay2 = QHBoxLayout() # repetição da configuração dos lay com criação
        self.tamanho_lay(self.lay2)

        self.lay3 = QHBoxLayout() # repetição da configuração dos lay com criação
        self.tamanho_lay(self.lay3)

        self.lay4 = QHBoxLayout() # repetição da configuração dos lay com criação
        self.tamanho_lay(self.lay4)


        self.lay5 = QHBoxLayout() # repetição da configuração dos lay com criação
        self.tamanho_lay(self.lay5)

        self.lay6 = QHBoxLayout() # repetição da configuração dos lay com criação
        self.tamanho_lay(self.lay6)

        self.lay7 = QHBoxLayout() # repetição da configuração dos lay com criação
        self.tamanho_lay(self.lay7)

#--------------------------------------- colocando um dentro do outro----------------

        self.setCentralWidget(self.janela) # janela principal com seu elemento
        self.janela.setLayout(self.lay) # janela com seu lay principal

        self.lay.addLayout(self.lay6) # colocando os lays secundarios dentro do principal
        self.lay.addLayout(self.lay7)
        self.lay.addLayout(self.lay1)
        self.lay.addLayout(self.lay2)
        self.lay.addLayout(self.lay3)
        self.lay.addLayout(self.lay4)
        self.lay.addLayout(self.lay5)




        self.botao1 = QPushButton("+")
        self.tamanho_botao(self.botao1)
        self.botao1.clicked.connect(lambda : self.sinal_soma("+")) #chama a aperação

        self.botao2 = QPushButton("-")
        self.tamanho_botao(self.botao2)
        self.botao2.clicked.connect(lambda: self.sinal_soma("-"))

        self.botao3 = QPushButton("*")
        self.tamanho_botao(self.botao3)
        self.botao3.clicked.connect(lambda: self.sinal_soma("*"))


        self.botao4 = QPushButton("/")
        self.tamanho_botao(self.botao4)
        self.botao4.clicked.connect(lambda: self.sinal_soma("/"))

        self.botao5 = QPushButton("=")
        self.tamanho_botao(self.botao5)
        self.botao5.clicked.connect(lambda: self.n1_igual())

        self.botao6 = QPushButton("1")
        self.tamanho_botao(self.botao6)
        self.botao6.clicked.connect(self.n1)

        self.botao7 = QPushButton("2")
        self.tamanho_botao(self.botao7)
        self.botao7.clicked.connect(self.n2)

        self.botao8 = QPushButton("3")
        self.tamanho_botao(self.botao8)
        self.botao8.clicked.connect(self.n3)

        self.botao9 = QPushButton("4")
        self.tamanho_botao(self.botao9)
        self.botao9.clicked.connect(self.n4)


        self.botao10 = QPushButton("%")
        self.tamanho_botao(self.botao10)


        self.botao11 = QPushButton("5")
        self.tamanho_botao(self.botao11)
        self.botao11.clicked.connect(self.n5)


        self.botao12 = QPushButton("6")
        self.tamanho_botao(self.botao12)
        self.botao12.clicked.connect(self.n6)

        self.botao13 = QPushButton("7")
        self.tamanho_botao(self.botao13)
        self.botao13.clicked.connect(self.n7)

        self.botao14 = QPushButton("8")
        self.tamanho_botao(self.botao14)
        self.botao14.clicked.connect(self.n8)

        self.botao15 = QPushButton("rad")
        self.tamanho_botao(self.botao15)

        self.botao16 = QPushButton("9")
        self.tamanho_botao(self.botao16)
        self.botao16.clicked.connect(self.n9)

        self.botao17 = QPushButton()
        self.tamanho_botao(self.botao17)
        self.botao18 = QPushButton()
        self.tamanho_botao(self.botao18)
        self.botao19 = QPushButton()
        self.tamanho_botao(self.botao19)
        self.botao20 = QPushButton()
        self.tamanho_botao(self.botao20)
        self.label1 = QLabel()
        self.label1.setText("Resultado")

        self.label2 = QLabel()
        self.label2.setText("0")

        self.tamanho_lab(self.label2)



        self.lay6.addWidget(self.label1)
        self.lay7.addWidget(self.label2)

        self.lay1.addWidget(self.botao1)
        self.lay1.addWidget(self.botao2)
        self.lay1.addWidget(self.botao3)
        self.lay1.addWidget(self.botao4)
        self.lay1.addWidget(self.botao5)

        self.lay2.addWidget(self.botao6)
        self.lay2.addWidget(self.botao7)
        self.lay2.addWidget(self.botao8)
        self.lay2.addWidget(self.botao9)
        self.lay2.addWidget(self.botao10)

        self.lay3.addWidget(self.botao11)
        self.lay3.addWidget(self.botao12)
        self.lay3.addWidget(self.botao13)
        self.lay3.addWidget(self.botao14)
        self.lay3.addWidget(self.botao15)

        self.lay4.addWidget(self.botao16)
        self.lay4.addWidget(self.botao17)
        self.lay4.addWidget(self.botao18)
        self.lay4.addWidget(self.botao19)
        self.lay4.addWidget(self.botao20)

    def tamanho_lay(self, lay):
        self.lay.setSpacing(3)

    def tamanho_botao(self, botao):
        botao.setStyleSheet('background-color: blue; color: black')

    def tamanho_lab(self, botao):
        botao.setStyleSheet('background-color: blue; color: black')

        # será necessária a criação de uma lista para armazenar os números digitados
        self.lista_numeros = []

        # será necessária a criação de um variavel para armazenar o sinal ,o valor será dado pelo
        # sinal e visto a cada nova pressionada
        self.sinal = float()

        # será necessária a criação de um lista de inteiros para armazenar os 2 números
        self.inteiros = []

        # criar uma lista de string, essa lista será zerada no sinal
        self.digitados=""



#criar uma função que imprima os numeros que estão sendo digitados


    def imprime_na_tela(self,numero):
        self.digitados+=numero
        print("\n" * 30)
        self.label2.setText(self.digitados)



#criar as operações entre os 2 números

    def men(self):
        return self.inteiros[0]-self.inteiros[1]
    def mult(self):
        return self.inteiros[0]*self.inteiros[1]
    def div(self):
        return self.inteiros[0]/self.inteiros[1]
    def som(self):
        return self.inteiros[0]+self.inteiros[1]

# criar uma função para cada número aqui poderemos ter um conjunto de funções
    # disparadas pelo número
    def n1(self):
        a="1"
        self.lista_numeros.append(a)
        self.imprime_na_tela(a)


    def n2(self):
        self.lista_numeros.append("2")
        a = "2"
        self.imprime_na_tela(a)

    def n3(self):
        self.lista_numeros.append("3")
        a = "3"
        self.imprime_na_tela(a)

    def n4(self):
        self.lista_numeros.append("4")
        a = "4"
        self.imprime_na_tela(a)

    def n5(self):
        self.lista_numeros.append("5")
        a = "5"
        self.imprime_na_tela(a)

    def n6(self):
        self.lista_numeros.append("6")
        a = "6"
        self.imprime_na_tela(a)


    def n7(self):
        self.lista_numeros.append("7")
        a = "7"
        self.imprime_na_tela(a)

    def n8(self):
        self.lista_numeros.append("8")
        a = "8"
        self.imprime_na_tela(a)

    def n9(self):
        self.lista_numeros.append("9")
        a = "9"
        self.imprime_na_tela(a)

    def n10(self):
        self.lista_numeros.append(".")

    def n1_igual(self):
        self.conferir_lista(self.inteiros,self.sinal)



    def sinal_soma(self,sin): # função acionada com ols botões de operações

        self.concatena_elementos() # aqui acrecentamos na lista inteiro um número caso exista o número
        print("\n" * 30)
        self.digitados = f"{self.digitados} {sin} " # aqui ele troca o valor pelo digito mais o sinal e ele subira assim
        print(self.digitados)
        self.label2.setText(self.digitados)
        if self.quantidade_na_lista():
            resultado=self.calculo(self.sinal)
            print("\n" * 30)
            self.digitados = f" {resultado} {sin} "  # aqui ele troca o valor pelo resultado mais o sinal e ele subira assim
            print(self.digitados)
            self.label2.setText(self.digitados)

        self.sinal = sin

    def conferir_lista(self,inteiros, sinal):
        self.concatena_elementos()
        print(self.sinal, " ", self.inteiros)
        if len(inteiros) == 2:
            if sinal == "+":
                resultado = self.som()
                self.label2.setText(str(resultado))

            elif sinal == "-":
                resultado = inteiros[0] - inteiros[1]
                self.label2.setText(str(resultado))

            elif sinal == "*":
                resultado = inteiros[0] * inteiros[1]
                self.label2.setText(str(resultado))

            elif sinal == "/":
                resultado = inteiros[0] / inteiros[1]
                self.label2.setText(str(resultado))
            self.inteiros=[]
            self.digitados=""
            self.lista_numeros=[]



    # função que crie os float e o armazene na lista de inteiros, ela será disparada pelo
    # sinal e precisará ser zerada no final a lista_números
    def concatena_elementos(self):
        concatena = ""
        if self.lista_numeros!=[]:  #confere se a lista está cheia ,caso esteja vazia ele não leva número
                                    #para lista, deixando ela da mesma forma

          a=self.lista_numeros   # pega os números da lista  para transformar em um inteiro
          for x in a:
            concatena += x

          self.lista_numeros=[] # aqui nós zeramos a lista de números , pois usaremos ela depois do uso do sinal
          concatena = int(concatena)

          self.inteiros.append(concatena) #acrecentamos na lista inteiros o número


# função para verificar se possui dois floats dentro da lista
    def quantidade_na_lista(self):
        if len(self.inteiros) == 2:
            return True
        return False





# função para realizar o cálculo caso exista 2 floats, esse calculo será enviado para
    # lista de floats que precisará ser zerada para recebe-lo
    def calculo(self,operacao):
        lista = {"+": self.som(), "-": self.men(), "*": self.mult(), "/": self.div()}
        resultado = lista[operacao]
        self.inteiros=[]
        self.inteiros.append(resultado)
        print(resultado)
        return resultado










if __name__=="__main__":
 app=QApplication(sys.argv)
 window=MainWindow()
 window.show()
 app.exec()