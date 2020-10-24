def inverte_dicionario(dic):
    dic2={}
    lista=dic.keys()
    lista1=dic.values()
    for i in lista:
        for j in lista1:
            dic2[lista1[j]]=lista[i]
    return dic2
    
