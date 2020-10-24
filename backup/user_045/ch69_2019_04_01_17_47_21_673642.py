def junta_listas(n):
    i=0
    
    l=[]
    while i<len(n):
        t=0
        while t<len(n[i]):
            l.append(n[i][t])
            t+=1
        i+=1
    return l
        
            
    
