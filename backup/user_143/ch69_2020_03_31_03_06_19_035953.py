def junta_listas(l):
    i=0
    lista=[0]
    while i<len(l):
        b=0
        d=l[i]
        while b<len(d):
            c=d[b]
            lista.append(c)
            b+=1
        i+=1
    return lista
            
                    
        