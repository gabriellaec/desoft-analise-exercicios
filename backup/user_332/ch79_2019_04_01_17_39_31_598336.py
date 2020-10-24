def monta_dicionario (lista1, lista2):
    dicionario = dict()
    i = 0
    for e in lista1:
        x = lista2[i]
        dicionario[e] = x
        i += 1
    return dicionario