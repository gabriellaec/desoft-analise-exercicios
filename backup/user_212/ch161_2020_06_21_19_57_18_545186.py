def PiWallis(n):
    numerador = 0
    denominador = 1
    produto = 1
    
    for i in range(n):
        
        if i%2 != 0:
            numerador += 2 
            produto = produto * (numerador/denominador)
         
        if i%2 == 0:
            denominador +=2
            produto = produto * (numerador/denominador)
            
    pi = produto * 2
    
    return pi
        
    
    
    
    
    
    
    
    
    