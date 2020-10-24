def verifica_primos(lista):
    d={}
    primo=True
    s=2
    for e in lista:
        while s<e:
            if e%s==0:
                primo=False
            d[e]=primo
            s+=1
    return d
       
       

    
   
            
