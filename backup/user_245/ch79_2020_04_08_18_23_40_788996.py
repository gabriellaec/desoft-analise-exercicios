def monta_dicionario(lista1,lista2):
    dici = {}
    for e in range(len(lista1)):
        dici[lista1[e]] = lista2[e]
    return dici