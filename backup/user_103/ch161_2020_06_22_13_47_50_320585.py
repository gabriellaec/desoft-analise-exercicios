def PiWallis(n):
    total= 2.0 
    if n == 1 :
        return 4.0
    for i in range(1,n):
        esquerda = float((2 * i)/(2 * i - 1))
        direita = float ((2 * i)/(2 * i + 1))
        total =  esquerda * direita
        total*=total
    return total
                    
        
        
    