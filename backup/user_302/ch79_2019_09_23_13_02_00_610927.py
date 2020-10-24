def monta_dicionario(lista1, lista2):
    i = 0
    dicionario=[]
    while i<len(lista1):
        dicionario[lista2[i]] = lista1[i]
        i += 1
    return dicionario
     