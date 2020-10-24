def monta_dicionario (lista, lista2):
    dicionario = {}
    i = 0
    while i < len(lista):
        dicionario[lista[i]] = lista2[i]
        i += 1
    return dicionario
    