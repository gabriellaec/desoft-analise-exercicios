def eh_primo(n) :
    
    ímpares = 3
    condicão  = True
    
    if n == 2:
        condicão = False
        n = True
    
    elif n % 2 != 0 :
        while condicão :
            cálculo = n % ímpares
         
            if cálculo == 0 :
                condicão = False
                n = False
            
            else :
                if ímpares < n :
                    ímpares += 2
                else:
                    condicão = False
                    n = True
    else:
        n = False
    
    return (n)