def eh_primo(n) :
    
    if n == 2 :
        return True
    
    elif n == 1 :
        return False    
    
    else :
        if n % 2 == 0:
            return False
                
        else:
            ímpares = 3
            while ímpares < n:
                
                if n % ímpares != 0:
                    ímpares += 2
                
                else:
                    return False
            else: 
                return True
            