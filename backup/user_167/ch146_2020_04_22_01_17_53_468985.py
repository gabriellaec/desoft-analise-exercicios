def conta_ocorrencias (lista):
    dic={}
    for e in range(o,len(lista)):
        if e in dic:
            dic[e]+=1
        else:
            dic[e]=1
    return dic 

        

        
    