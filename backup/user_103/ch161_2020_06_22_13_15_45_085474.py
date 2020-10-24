def PiWallis(n):
    pi = 0.0
    for i in range(n):
        esquerda = float((2 * i)/(2 * i - 1))
        direita = float ((2 * i)/(2 * i + 1))
        total = esquerda * direita
        pi = pi + total

    return pi
                    
        
        
    