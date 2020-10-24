def monta_dicionario(lista1, lista2):
    dici = {}
    i = 0
    while i < len(lista1):
        dici[lista1[i]] = lista2[i]
        i += 1
    return dici