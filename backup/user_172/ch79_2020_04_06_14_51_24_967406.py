def monta_dicionario (lista1, lista2):
    x = len(lista1)
    y = len(lista2)
    x=y
    dicionario = {}
    a = 0
    b = 0
    for a in lista1:
        for b in lista2:
            dicionario[a] = b
    return dicionario