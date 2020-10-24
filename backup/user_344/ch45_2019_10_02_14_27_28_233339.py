def num_pos(lista):
    i=0
    vp =[]
    while i<len(lista):
        if lista[i]>0:
            vp.append(lista[i])
        i+=1    
    return vp