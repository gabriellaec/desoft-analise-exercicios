def monta_dicionario(lista1,lista2):
    dic={}
    for i in lista1:
        for i in lista2:
            dic[lista1[i]]=lista2[i]
    return dic
       