def lista_primos(x) :
    
    lista = [0]*x
    lista[0] = 2
    lista[1] = 3
    i = 2
    ímpares = 3
    
    while  < x:
        
        if (lista[i-1] + 1) % 2 == 0 :
            i += 1
        
        else: 
           
            while ímpares < (lista[i-1] + 1) and (lista[i-1] + 1) % 2 != 0 :
                
                ímpares += 2
            
            else:   
                lista[i] = lista[i-1] + 1
                i += 1
    
    return lista
            