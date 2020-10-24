def conta_ocorrencias(lista):
    dic={}
    i=1
    for itens in lista:
        if itens in dic:
            dic[itens]+=1 
        else:
            dic[itens]=1
            
    return dic
      