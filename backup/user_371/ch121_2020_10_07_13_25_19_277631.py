def subtracao_de_listas(lista1,lista2):
    i=0
    lista_nova=[]
    while len(lista1)>i:
        if lista1[i] not in lista2:
            lista_nova.append(lista1[i])
        i+=1
    return lista_nova