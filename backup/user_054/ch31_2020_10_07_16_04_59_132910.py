def eh_primo (n):
    if n == 0 or n == 1 or n == 2:
        return False
    elif n%2 == 0 and n > 2:
        return False
    else:
        i = 3
        while i <= n:
            if n%i == 0:
                return False
            i+=2
    return True
            
            
        
    