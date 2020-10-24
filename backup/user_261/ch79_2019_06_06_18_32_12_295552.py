def monta_dicionario(lista1,lista2):
    dic={}
    elementoslista2=[]
    i=0
    for chaves in lista1:
        dic[chaves]=lista2[i]
        i+=1
    return dic
