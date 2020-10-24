def PiWallis(precisao):
    
    mudar_denominador = False
    mudar_numerador = False
    
    denominador = 1
    numerador = 2
    
    resultado = 1
    
    for n in range(1, precisao + 1):
        
        resultado *= numerador / denominador
        
        if n % 2 == 1: denominador += 2
        else: numerador += 2
    
    return resultado * 2
        
        
        
        