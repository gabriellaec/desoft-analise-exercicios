def zera_negativos(lista):
    i=0
    vp =[0]
    while i<len(lista):
        if lista[i]>0:
            vp.append(lista[i])
        i+=1    
    return vp