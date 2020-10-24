def eh_primo(x):
    if x == 2:
        return True
    elif x == 1:
        return False
    elif x == 0:
        return False
    elif x%2 == 0:
        return False
    else: 
        n = 2
        while n < x:
            if x%n != 0:
                return True
            n = n + 2
                return False
            
        
    