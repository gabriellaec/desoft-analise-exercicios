def monta_dicionario(lista1, lista2):
    i=0
    while i<len(lista1):
        dicio={}
        dicio[lista1[i]]=lista2[i]
        i=i+1
    return dicio