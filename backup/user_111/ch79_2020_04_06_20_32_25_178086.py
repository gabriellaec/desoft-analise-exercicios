def monta_dicionario(lista1,lista2):
    dicionario={}
    for i in range(0,len(lista2)):
        dicionario[lista1[i]]=lista2[i]
    return dicionario