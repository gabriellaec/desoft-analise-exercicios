def lista_primos(x) :
    
    lista = [0]*x
    lista[0] = 2
    lista[1] = 3
    i = 2
    a = 1
    while i < x:
        ímpares = 3
        
        if (lista[i-1] + a) % 2 == 0 :
            a += 1
        
        else: 
            while ímpares < (lista[i-1] + a) and (lista[i-1] + a) % 2 != 0 :
                
                if (lista[i-1] + a) % ímpares != 0:
                    ímpares += 2
                
                else:
                    a = 1
            
            else:   
                lista[i] = lista[i-1] + a
                i += 1
                a = 1
                
    
    return lista