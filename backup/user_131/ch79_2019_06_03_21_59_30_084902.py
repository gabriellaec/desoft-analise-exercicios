def monta_dicionario(lista1, lista2):
    dicionario = dict()
    i=0
    while i < len(lista1):
        dicionario[lista1[i]]=lista2[i]
        i = i+1  
    return dicionario