def monta_dicionario(lista1, lista2):
    i=0
    dicionario= dict()
    while i<len(lista1):
        dicionario[lista1[i]] = lista2[i]
        i+=1
    return dicionario