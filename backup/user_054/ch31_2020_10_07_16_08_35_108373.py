def eh_primo (n):
    if n == 2:
        return True
    if n == 0 or n == 1:
        return False
    elif n%2 == 0 :
        return False
    else:
        i = 3
        while i <= n and n > 2:
            if n%i == 0:
                return False
            i+=2
    return True
            
            
        
    