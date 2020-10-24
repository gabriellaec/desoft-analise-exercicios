def verifica_primos(lista):
    d={}
    for e in lista:
        if e%2==0 and e!=2:
            d[e]=False
        else:
            d[e]=True
    return d

    
   
            
