def junta_listas(l):
    i = 0
    new_l = []
    while i<len(l):
        t= 0
        while t < len(l[i]):
            new_l.append(l[i][t])
            t+=1
        i += 1
    return new_l
            
       
        