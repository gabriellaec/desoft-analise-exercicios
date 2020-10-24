def verifica_primos(lista):
    d={}
  
    for e in lista:
        if e>=0:
            for i in range(2,e-1):
                if e%i==0 and e!=2:
                    d[e]=False
                else:
                    d[e]=True
           
        else:
            d[e]=True
    return d

    
   
            
