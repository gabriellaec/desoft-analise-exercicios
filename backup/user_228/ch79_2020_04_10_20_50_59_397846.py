def monta_dicionario(lista1,lista2):
    dic={}
    for i in lista1:
        for o in lista2:
        dic[lista1[i]]=lista2[o]
    return dic
       