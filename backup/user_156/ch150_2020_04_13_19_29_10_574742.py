def calcula_pi(numero):
    
    i = 1
    soma = 0
    
    while (i-1) < numero:
        soma += 6/(i**2)
        i += 1
        
    return soma**0.5
    
    
    