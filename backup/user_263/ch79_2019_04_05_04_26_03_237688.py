def monta_dicionario(lista1,lista2):
    dic={}
    i=0
    for e in lista1:
        dic[e]=lista2[i]
        i+=1
    return dic
        