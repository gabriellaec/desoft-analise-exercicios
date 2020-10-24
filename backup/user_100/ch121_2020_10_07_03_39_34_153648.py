def subtracao_de_listas(lista1,lista2):
    lista3 = []
    #c = contador
    c = 0
    while c < len(lista1):
        if lista1[c] not in lista2:
            lista3.append(lista1[c])
            c = c + 1
        else:
            c = c + 1
    return lista3



        