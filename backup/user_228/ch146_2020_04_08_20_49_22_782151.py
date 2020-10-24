def conta_ocorrencias(lista):
    dic={}
    for i in lista:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return dic            
        
        