def monta_dicionario(lista1, lista2):
    dicionario = {}
    for d in range(len(lista1)):
        dicionario[lista1[d]] = lista2[d]
    return dicionario