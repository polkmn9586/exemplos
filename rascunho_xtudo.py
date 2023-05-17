import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove


dados={
        "hambúrguer":{
                       "x-salada":{"valor":10.00,"itens":["batata","molho"]}
                     },
        "cachorro_quente":{
                            "quente_vai":{"valor":10.00,"itens":["batata","molho"]}
                          }

      }


def adic_categoria(nome):
    dados[nome] = None

def adic_elementos():
    for x in dados:
        print(x)
    a=input("digite o local do produto")
    b=input("digite o nome do produto a acrescentar")

    dados[a][b]=None
    print(dados[a])

while True:
  adic_elementos()
  """adic_categoria(input("valor? "))
  for x in dados:
   print(x)"""


