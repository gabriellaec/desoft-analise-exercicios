def monta_dicionario(lista1,lista2):
    dicionario={}
    i=0
    for n in range (0,len(lista2)):
        dicionario[lista1[i]]=lista2[i]
        i+=1
    return dicionario
                     