def monta_dicionario (lista1,lista2):
    dicionário = dict()
    c = 0
    for i in lista1:
        dicionário[i] = lista2[i]
    return dicionário
