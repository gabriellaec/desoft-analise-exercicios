def monta_dicionario(lista1, lista2):
    dicionario=dict()
    for i in lista1:
        for i in lista2:
            dicionario[lista1[i]]=lista2[i]
    return dicionario
        