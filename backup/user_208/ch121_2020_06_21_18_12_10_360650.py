def subtracao_de_listas (lista1,lista2):
    lista= []
    i = 0
    while i < len(lista1) and i < len(lista2):
        if lista1[i] in lista2:
            lista.append(lista1[i])
        i+=1
    return lista