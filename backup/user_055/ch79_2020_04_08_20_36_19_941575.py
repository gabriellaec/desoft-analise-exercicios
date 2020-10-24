def monta_dicionario(lista_a, lista_b):
    dicionario = {}
    for i in range(len(lista_a)):
        dicionario[lista_a[i]] = lista_b[i]
    return dicionario