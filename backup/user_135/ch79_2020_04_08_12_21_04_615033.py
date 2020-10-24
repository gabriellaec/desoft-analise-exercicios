def monta_dicionario(lista1, lista2):
    dicionario = {}
    for indice in range(int(len(lista1))):
        dicionario[lista1[indice]] = lista2[indice]
    return dicionario