def monta_dicionario(lista1, lista2):
    novo_d = {}
    for k in lista1:
        for v in lista2:
            novo_d[k] = v
    return novo_d