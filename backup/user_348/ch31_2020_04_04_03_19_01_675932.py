def eh_primo (n):
    p = 3
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    else:
        while n>=3:
            if (n%2==0) or (n%p == 0):
                p = p + 2
                return False
            else:
                return True
        
    
        