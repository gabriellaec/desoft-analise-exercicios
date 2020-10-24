def verifica_primos(lista):
    d={}
    i=2
    for e in lista:
        if e>0:
        while i<lista[e]:
            if e%i==0 and e!=2:
                d[e]=False
            else:
                d[e]=True
            i+=1
        else:
            d[e]=True
    return d

    
   
            
