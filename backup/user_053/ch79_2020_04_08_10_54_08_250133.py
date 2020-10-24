def monta_dicionario(lista_1, lista_2):
    dicionario = dict()
    for i in range(0, len(lista_1)):
        dicionario[lista_1[i]] = lista_2[i]
    return dicionario