def eh_primo (n):
    p = 3
    if n == 0 or n == 1 or (n%2==0):
        return False
    elif (n%2==0):
        return True
    else:
        while n>p:
            if (n%2==0):
                return False
            else:
                p = p + 2
        return True
                
        
    
        