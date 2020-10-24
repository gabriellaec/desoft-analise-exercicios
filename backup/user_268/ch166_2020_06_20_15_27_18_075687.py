def total_do_semestre_por_bairro(dt):
    
    c = dt.keys()
    v = dt.values()
    nv = []
    tst = []
    newd = {}
    print(len(c))

    for i in c:
        tst.append(i)

    for i in v: 
        gasto = 0 
        
        for j in range(6, 12): 
            gasto += i[j]
            
        nv.append(gasto)  

    print(nv)
    
    for i in range(len(tst)):

        newd[tst[i]] = nv[i]
        
    return newd
        
        
        
        
    