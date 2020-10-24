def junta_nomes(l1,l2,l3):
    lista = []
    a = 0
    b = 0
    
    i=0
    i2=0
    while i < len(l1)-1:
        if len(l1) > 0:
            lista.append(l1[i]+l3[a])
        a+=1
        i+=1
            
    for z in l2:
        if len(l2) > 0:
            lista.append(z+l3[b])
            b +=1
            
    return lista