def monta_dicionario(lista1, lista2):
    dict = {}
    i = 0
    for item in lista1:
        dict[item] = lista2[i]
        i += 1

    return dict