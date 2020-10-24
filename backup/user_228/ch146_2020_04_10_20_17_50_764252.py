def conta_ocorrencias(lista):
    dic={}
    i=0
    while i<len(lista):
        if i not in dic:
            dic[i]=1
            i+=1
        else:
            dic[i]+=1
            i+=1
    return dic            
        
        