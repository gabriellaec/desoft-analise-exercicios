def acha_bigramas(l):
    bi = []
    for i in range(1,len(l)):
        bigrama = l[i-1]+l[i]
        if bigrama not in bi:
            bi.append(bigrama)
   
            
    return bi