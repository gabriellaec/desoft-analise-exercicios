def conta_ocorrencias(lista):
    dic={}
    i=2
    for itens in lista:
        if itens not in dic.keys():
            dic[itens]=1
        else:
            dic[itens]=i
            i+=1
    return dic
        
        
     