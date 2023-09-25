




def listas_5():
    from random import randint
    lista1=[]
    for x in range(100):
        lista1.append(randint(1,25))

    lista2=[]
    for x in range(100):
        lista2.append(randint(1,25))

    lista3=[]
    for x in range(100):
        lista3.append(randint(1,25))

    lista4=[]
    for x in range(100):
        lista4.append(randint(1,25))

    lista5=[]
    for x in range(100):
        lista5.append(randint(1,25))
    return [lista1,lista2,lista3,lista4,lista5]
def treino_grupos_sorteados_juntos(lista):
    lista1,lista2,lista3,lista4,lista5=lista
    menor=15
    maior=20
    recebe=[]
    cont=10
    global numeros_sorteados
    while cont<=len(lista2):
      numeros_sorteados=[]
      try:

        numero_na_lista1=lista1[cont]# Número escolhido
        numero_index1=lista1[cont-1::-1].index(numero_na_lista1)# Tempo que demorou para repetir
        if numero_index1>=menor and numero_index1<=maior: # número que será aceito
           numeros_sorteados.append({numero_na_lista1:"lista1"}) #colocando numero na lista recente

      except:
          ...
      try:
        numero_na_lista2 = lista2[cont] # Número escolhido
        numero_index2 = lista2[cont - 1::-1].index(numero_na_lista2)
        if numero_index2 >= menor and numero_index2 <= maior:
            numeros_sorteados.append({numero_na_lista2:"lista2"})  # colocando numero na lista recente

      except:
          ...
      try:
        numero_na_lista3 = lista3[cont]  # Número escolhido
        numero_index3 = lista3[cont - 1::-1].index(numero_na_lista3)
        if numero_index3 >= menor and numero_index3 <= maior:
            numeros_sorteados.append({numero_na_lista3:"lista3"})  # colocando numero na lista recente

      except:
          ...
      try:

        numero_na_lista4 = lista4[cont]  # Número escolhido
        numero_index4 = lista4[cont - 1::-1].index(numero_na_lista4)
        if numero_index4 >= menor and numero_index4 <= maior:
            numeros_sorteados.append({numero_na_lista4:"lista4"})  # colocando numero na lista recente
      except:
          ...
      try:
        numero_na_lista5 = lista5[cont]  # Número escolhido
        numero_index5 = lista5[cont - 1::-1].index(numero_na_lista5)
        if numero_index5 >= menor and numero_index5 <= maior:
            numeros_sorteados.append({numero_na_lista5:"lista5"})  # colocando numero na lista recente

        if len(numeros_sorteados)>= 3:
            """print(f"Lista: lista2 , posição: {cont} , numero : {numero_na_lista2} , atraso: {numero_index2}")
            print(f"Lista: lista1 , posição: {cont} , numero : {numero_na_lista1} , atraso: {numero_index1}")
            print(f"Lista: lista2 , posição: {cont} , numero : {numero_na_lista3} , atraso: {numero_index3}")
            print(f"Lista: lista1 , posição: {cont} , numero : {numero_na_lista4} , atraso: {numero_index4}")
            print(f"Lista: lista1 , posição: {cont} , numero : {numero_na_lista5} , atraso: {numero_index5}")"""

            print(numeros_sorteados)
        cont += 1

      except:
          cont+=1
          ...


treino_grupos_sorteados_juntos(listas_5())
