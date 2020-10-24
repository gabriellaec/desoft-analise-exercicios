def junta_nomes(l1,l2,l3):
    lista = []

    for c in l1:
        if len(l1) > 0:
            for x in l3:
                lista.append(c+x)    
    for z in l2:
        if len(l2) > 0:
            for t in l3:
                lista.append(z+t)            
    return lista