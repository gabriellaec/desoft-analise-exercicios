def zera_negativos(lista):
    i=0
    vp =[]
    if lista[i] == 0:
        vp.append(0)
    
    while i<len(lista):
        if lista[i]>0:
            vp.append(lista[i])
        i+=1  
        
            
    return vp