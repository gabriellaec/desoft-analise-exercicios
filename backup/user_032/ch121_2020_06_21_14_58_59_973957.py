def subtracao_de_listas(lista1,lista2):
    lista = []
    for x in lista1:
        if x not in lista2 and x not in lista:
            lista.append(x)
    return lista