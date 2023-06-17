from funcao_com_json import lendo_arquivo_json_ , lendo_arquivo_json_dic

casa=lendo_arquivo_json_("loja.json")
dicionario=""
lista=""
for x in casa.keys():
    if casa[x] != {}:
     casa1=casa[x]
     lista+=f"{x}: "
     for b in casa1:
         lista+=f"{b}, "
     lista+="\n"
     dicionario=lista

