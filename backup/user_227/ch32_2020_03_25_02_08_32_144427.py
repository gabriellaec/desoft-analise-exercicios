def lista_primos(x) :
    
    lista = [0]*x
    lista[0] = 2
    lista[1] = 3
    i = 2
    ímpares = 3
    a = 1
    while i < x:
        ímpares = 3
        consecutivo = lista[i-1] + a
        
        if consecutivo % 2 != 0:
            condicao = True
            while condicao :
                 while ímpares < consecutivo and condicao:
                     if consecutivo % ímpares != 0 :
                        ímpares += 2
                     else:
                         a += 1
                         condicao = False
                    
                 if consecutivo == ímpares : 
                     lista[i] = consecutivo
                     a = 1
                     i += 1 
                     condicao = False 
                    
            else:
                a += 1
                    
        else:
            a += 1
            
    return lista