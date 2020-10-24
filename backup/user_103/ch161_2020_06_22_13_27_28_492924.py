def PiWallis(n):
    if n == 1 :
        return 4.0
    for i in range(n):
        esquerda = float((2 * i)/(2 * i - 1))
        direita = float ((2 * i)/(2 * i + 1))
        total = pi* esquerda * direita
        total*=total
    return total
                    
        
        
    