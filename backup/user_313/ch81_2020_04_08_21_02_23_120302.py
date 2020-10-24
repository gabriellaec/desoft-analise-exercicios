def interseccao_chaves(l1,l2):

    lista= []
    for k, v in l1.items():
        
        lista.append(v)
    
    
    
    novalista= []
    
    for i in l2:
        a = l2[i]
        
        for b in lista:
            if a == b:
                novalista.append(a)
    return novalista