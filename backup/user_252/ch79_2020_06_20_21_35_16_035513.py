def monta_dicionario(lista1, lista2):
    dicionario={}
    for i in range(len(lista1)):
        x=lista1[i]
        y=lista2[i]
        dicionario[x]=y
    return dicionario