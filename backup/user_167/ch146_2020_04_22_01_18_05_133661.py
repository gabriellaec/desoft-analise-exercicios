def conta_ocorrencias (lista):
    dic={}
    for e in range(0,len(lista)):
        if e in dic:
            dic[e]+=1
        else:
            dic[e]=1
    return dic 

        

        
    