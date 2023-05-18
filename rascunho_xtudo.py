
casa={
  "hambúrguer": {
    "produto": {
      "valor": 10,
      "itens": []
    }
  },"sapo": {
    "produto": {
      "valor": 10,
      "itens": []
    }
  }}

casa["hambúrguer"]["produto1"]={"oi":"pp","cad":"oo"}
casa["hambúrguer"]["produto2"]={"oi":"pp","cad":"oo"}
if casa["sapo"]==None:
 casa["sapo"]={"produto1":{"oi":"pp","cad":"oo"}}
else:
  casa["sapo"]["produto1"]= {"oi": "pp", "cad": "oo"}
print(casa)





