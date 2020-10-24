def primeiras_ocorrencias(string):
    dic={}
    lista=[]
    for i in string:
        if i not in lista:
            lista.append(i)
            dic[i]=string.index(i)
    return dic
        
    