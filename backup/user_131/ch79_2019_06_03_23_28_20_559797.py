def monta_dicionario(lista1, lista2):
    dicionario = dict()
    for e in lista1:
        dicionario[lista1[e]]=lista2[e]
    return dicionario