def monta_dicionario (lista1, lista2):
    x = len(lista1)
    y = len(lista2)
    x=y
    dicionario = {}
    for i in range(len(lista1)):
        a = lista1[i]
        b = lista2[i]
        dicionario[a] = b
    return dicionario