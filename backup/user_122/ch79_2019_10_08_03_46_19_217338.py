def monta_dicionario(lista1, lista2):
    for l1, l2 in lista1, lista2:
        dicionario = dict(l1, l2)
    return dicionario