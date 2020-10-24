def conta_bigramas(texto):
    dic={}
    for i in range(len(texto-1):
        bigrama=texto[i]+texto[i+1]
        if bigrama not in dic:
            dic[bigrama]=1
        else:
            dic[bigrama]+=1
    return dic
    
            
          
            
