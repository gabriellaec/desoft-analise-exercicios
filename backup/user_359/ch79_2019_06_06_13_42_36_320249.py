def monta_dicionario(lista1, lista2):
    novo_d = {}
    i=0
    while i != len(lista1):
        novo_d[lista1[i]] = lista2[i]
        i += 1
    return novo_d