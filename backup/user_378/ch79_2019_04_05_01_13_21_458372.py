def monta_dicionario(lista_1,lista_2):
    dic={}
    k=0
    for i in lista_2:
        dic[lista_1[k]]=lista_2[k]
        k+=1
    return dic
