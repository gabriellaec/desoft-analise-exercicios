def eh_primo (n):
    p = 3
    if n == 0 or n == 1 
        return False
    elif n == 2:
        return True
    else:
        while n>p:
            if (n%2==0):
                p = p + 1
                return False
            else:
                return True
        
    
        