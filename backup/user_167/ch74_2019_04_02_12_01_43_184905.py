def conta_bigramas(n):
    d={}
    for e in range (len(n)-1):
        bigrama=n[e:e+2]
        d[bigrama]=0
    for e in range(len(n)-1):
        bigrama=n[e:e+2]
        d[bigrama]+=1
    return d
        
      
    
        
       