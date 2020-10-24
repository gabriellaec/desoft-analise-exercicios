def monta_dicionario(lista1, lista2):
    dic = {}
    cont = 0
    while cont < len(lista1):
        dic[lista1[cont]] = lista2[cont]
        cont += 1
    return dic
