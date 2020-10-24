def eh_primo(n) :
    
    if n == 2 :
        n = True
    
    
    else :
        condicão = True
        ímpares = 3
        while condicão :
            cálculo = n % ímpares
            
            if n % 2 == 0:
                n = False
                condicão = False
               
            
            elif cálculo == 0 :
                n = False
                condicão = False
                

            elif ímpares < n :
                ímpares += 2
            
            else:
                n = True
                condicão = False
    
    return (n)