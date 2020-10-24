def monta_dicionario(lista1,lista2):
    dic={}
    elementoslista2=[]
    for chaves in lista2:
    elementoslista2.append(chaves) 
    for chaves in lista1:
        i=0
        dic[chaves]=elementoslista2[i]
        i+=1
    return dic
