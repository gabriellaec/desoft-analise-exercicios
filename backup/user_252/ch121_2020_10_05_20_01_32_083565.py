def subtracao_de_listas (lista1, lista2):
    lista_final=[]
    i=0
    while i < len(lista1):
        if lista1[i] not in lista2:
            lista_final.append(lista1[i])
        i+=1
    return lista_final