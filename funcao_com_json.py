import json
from copy import deepcopy
import requests

def lendo_arquivo_json_(arquivo_nome):
    """ permite a leitura de um arquivo .json entregando o seu resultado, caso ele não exista ou esteje vazio será criado um com []
        e assim entregue no primeiro momento. Ele retorna uma lista.
         """
    try:
     with open(arquivo_nome, "r") as arquivo1: # fará a leitura do arquivo
       arquivo1.seek(0,0)
       recebe=json.load(arquivo1)         # recebe a leitura

       return recebe                     # retorna o arquivo json

    except:
        with open(arquivo_nome, "w", encoding='utf8') as arquivo2:
         json.dump([],arquivo2)
         return arquivo2

def escrevendo_json_novo(variavel,arquivo):
  """Cria um arquivo json novo e escreve nele"""
  with open(arquivo,"w",encoding='utf-8')as arquivo1:
      json.dump(variavel,arquivo1,ensure_ascii=False,indent=2)

def limp_tela():
    print("\n"*100)

def preenchimento_dicionario(lista_para_acrecentar): # estará dentro de uma lista esses dados
    contador = "s"
    print("vamos digitar os elementos")
    while True:
        ind = input("Digite o índice: ")
        if ind == "0":
            break
        valor = input("Digite o valor: ")
        if valor == "0":
            break
        limp_tela()
        print("Vamos para o próximo")
        lista_para_acrecentar.append({ind: valor})
    limp_tela()
    return lista_para_acrecentar


def eliminador_de_l_d(lista):
    """ Se a lista tiver como itens outras listas ela tornará esses elementos str e assim retornara uma lista única"""
    nova_lista=[]
    for x in lista:
        nova_lista=x
    return nova_lista

def consulta_str_em_lista (stringg,lista):
    """realiza a consulta de uma string dentro de uma lista retornando False ou True"""

    stringg=stringg.lower().strip()
    if stringg  in lista:
      return True
    return False
##---------------------------------
def adiciona_elemento_na_lista_json(elemento,arquivo):
 a=lendo_arquivo_json_(arquivo)
 a.append(elemento)
 escrevendo_json_novo(a,arquivo)

