def monta_dicionario(lista1, lista2):
    dicionario_montado = dict()
    i = 0
    while i < len(lista1):
        dicionario_montado[lista1[i]] = lista2[i]
        i += 1
    return dicionario_montado