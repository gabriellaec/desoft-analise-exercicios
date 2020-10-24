def monta_dicionario (lista1, lista2):
    x = len(lista1)
    y = len(lista2)
    x=y
    dicionario = {}
    for a in lista1:
        for b in lista2:
        dicionario[a] = b
    return dicionario