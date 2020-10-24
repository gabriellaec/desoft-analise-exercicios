def monta_dicionario (lista1, lista2):
    dicionario={}
    i=0
    while i < len(lista1):
        dicionario[lista1[i]]=lista2[i]
        i+=1
    return dicionario