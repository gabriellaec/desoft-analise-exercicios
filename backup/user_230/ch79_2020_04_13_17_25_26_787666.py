def monta_dicionario(lista1, lista2):
    dicionario=dict()
    for i in range(len(lista1)):
        for i in range(len(lista2)):
            dicionario[lista1[i]]=lista2[i]
    return dicionario
        