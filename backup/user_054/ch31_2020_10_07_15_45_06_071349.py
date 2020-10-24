def eh_primo (n):
    if n == 0 and n == 1:
        return False
    elif n%2 == 0:
        return False
    else:
        i = 3
        while i <= n:
            if n%i == 0:
                return False
            elif n%i == 1:
                return True
            i+=2
            
        
    