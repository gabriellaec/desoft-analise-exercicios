def monta_dicionario (lista1,lista2):
    dicionário = dict()
    c = 0
    for i in lista1:
        while True:
            dicionário[i] = lista2[c]
            break
    return dicionário
