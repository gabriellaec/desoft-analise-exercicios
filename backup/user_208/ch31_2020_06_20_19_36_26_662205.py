def eh_primo (n):
    if n == 1 or n == 0:
        return False
    else:
        y = 2    
        while n % y != 0 and y <= n/2:
            y+=1
        if n % y == 0:
            return False
        else:
            return True
    
                
   