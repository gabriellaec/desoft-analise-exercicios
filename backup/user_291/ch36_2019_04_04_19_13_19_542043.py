def eh_primo(numero):
    
    if numero <= 1:
        return False
    
    for e in range(2,numero):
        if(n % e == 0):
            return False
    return True
            
        