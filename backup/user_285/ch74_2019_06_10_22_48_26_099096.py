def conta_bigramas(palavra):
    dic={}
    for i in range(len(palavra)-1):
        if not palavra[i:i+2] in dic:
            dic[palavra[i:i+2]]=1
        else:
            dic[palavra[i:i+2]]+=1
    return dic

                    
    
                
        
    
                                 
        