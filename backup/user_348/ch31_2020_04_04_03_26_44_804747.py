def eh_primo (n):
    p = 3
    if n == 0 or n == 1:
        return False
    elif n == 2 or n ==3:
        return True
    else:
        while n>p:
            p = p + 2
            if (n%2==0) and (n%p == 0):
                return False
            else:
                return True
        
    
        