def conta_ocorrencias(lista):
    dic={}
    c=0
    for i in lista:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
            
    return dic            
        
        