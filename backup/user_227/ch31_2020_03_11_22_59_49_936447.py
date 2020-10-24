def eh_primo(n) :
    
    if n == 2 and n % 2 == 0 :
        n = True
    
    elif n % 2 != 0 and n != 1 :
        condicão = True
        ímpares = 3
        while condicão :
            cálculo = n % ímpares
            
            if cálculo == 0 :
                condicão = False
                n = False

            elif ímpares < n :
                ímpares += 2
            
            else:
                condicão = False
                n = True
    else:
        n = False
    
    return (n)
