def subtracao_de_listas(lista1, lista2):
    lista3= []
    i=0
    while i < len(lista2):  
        if lista2[i] not in lista1:
            lista3.append(lista2[i])
        i+= 1
    return lista3