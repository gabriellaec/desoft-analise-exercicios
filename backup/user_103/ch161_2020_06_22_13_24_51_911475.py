def PiWallis(n):
    for i in range(n):
        if n == 1 :
            return 4.0
        else:
            esquerda = float((2 * i)/(2 * i - 1))
            direita = float ((2 * i)/(2 * i + 1))
            total = esquerda * direita
            total*=total
        return total
                    
        
        
    