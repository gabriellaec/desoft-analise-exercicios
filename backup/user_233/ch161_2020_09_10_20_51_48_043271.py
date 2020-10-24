
def PiWallis(precisao):
    
    resultado = 1
    
    denominador = 1
    numerador = 2
    
    for n in range(1, precisao + 1):
        
        resultado *= numerador / denominador
        
        if n % 2 == 1: denominador += 2
        else: numerador += 2
    
    return resultado * 2
        