def monta_dicionario(lista1,lista2):
    dicionario={}
    i=0
    for lista1 in range(0,len(lista2)):
        dicionario[lista1[i]]=lista2[i]
        i+=1
    return dicionario
                     