def subtracao_de_listas (lista1,lista2):
    lista3 = []
    i = 0
    while i < len(lista1):
        if lista[i] not in lista2:
            lista3.append(lista[i])
        i += 1
    
    return lista3