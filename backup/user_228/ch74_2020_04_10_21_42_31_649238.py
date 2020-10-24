def conta_bigramas(texto):
    dic={}
    i=0
    while i<(len(texto)-1):
        bigrama=texto[i]+texto[i+1]
        i+=1
        if bigrama not in dic:
            dic[bigrama]=1
            i+=1
        else:
            dic[bigrama]+=1
            i+=1
    return dic
    
            
          
            
