import json
import requests
def leitor_api(url, headers=None):
    """Leitor de api, pega o url do Api e poderá retor  uma lista com itens que são arquivos json de cada página,
       quando a api está dividida em páginas ou um json único quando toda a informação se encontra em uma única
       página
        """
    payload = {}
    headers = {}
    lista_de_resutados=[]
    while url!=None:
     response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)
     lista_de_resutados.append(response)
     url=response["next"]
    if len(lista_de_resutados)>1:
        return lista_de_resutados
    else:
        return response

def escolhe_elementos(arquivo, local, elemento1, elemento2):
    """Pega 2 elementos , que são Keys de vários dicionários , esses dicionários compõe itens de uma lista e essa lista é
        um dos itens do arquivo json. Ele entregará esse elementos dentro de uma lista , os 2 elemetos são entregues como str"""
    recebe=arquivo[local]
    acumula=[]
    for i in recebe :
        acumula+=[f"{i[elemento1].strip().lower()} , {i[elemento2].strip().lower()}"]
    return acumula

def pega_1_elemento_lista_em_json(arquivo, item, elemento1):
 """Pega um elemento , que é Key de vários dicionários , esses dicionários compõe itens de uma lista e essa lista é
    um dos itens do arquivo json. Ele entregará esse elementos dentro de uma lista
 """
 if isinstance(arquivo, list ):
    recebe=arquivo[item]
    acumula=[]
    for i in recebe :
        acumula+=[i[elemento1].strip() ]
    return acumula

def resgata_2_elemento(endereco,local,element1,elemento2):
    mesa = leitor_api(endereco)
    elementos= escolhe_elementos(mesa, local,element1, elemento2)
    return elementos

def simples_json_end_verificao(url,headers=None,payload=None):
    """Imprimi na tela de forma organizada o que esta dentro de json"""
    payload = {payload}
    headers={headers}

    while url!=None:
     response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)
     response=dict(response)
     for i , x in response.items():
        if isinstance(x,list):
         print(i,":")
         for b in x:
             print(b)
        else:
             print(i, ": ", x)
     url=response["next"]




