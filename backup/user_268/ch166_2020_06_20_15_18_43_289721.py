def total_do_semestre_por_bairro(dt):
    
    c = dt.keys()
    v = dt.values()
    nv = []
    newd = {}
    
    for i in v: 
        gasto = 0 
        
        for j in range(6, 12): 
            gasto += i[j]
            
        nv.append(gasto)  
    
    for i in range(len(c)):
        newd[c[i]] = nv[i]
        
    return newd
    
            
            
            
            
        
        
        
        
    