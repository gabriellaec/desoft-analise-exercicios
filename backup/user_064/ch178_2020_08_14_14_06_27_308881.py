def junta_nomes(l1,l2,l3):
    lista = []
    a = 0
    b = 0
   
    for c in l1:
        if len(l1) > 0:
            lista.append(c+l3[a])
            a+=1
    for z in l2:
        if len(l2) > 0:
            lista.append(z+l3[b])
            b +=1
        
    
    return lista