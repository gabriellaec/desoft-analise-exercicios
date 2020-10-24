def monta_dicionario(lista1,lista2):
    dicionario = {}
    n = 0
    for i in lista1:
        dicionario[i] = lista2[n]
        n += 1
    return dicionario