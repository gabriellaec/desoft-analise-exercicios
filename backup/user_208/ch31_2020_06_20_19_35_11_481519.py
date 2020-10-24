def eh_primo (n):
    y = 2
    while n % y != 0 and y <= n/2:
        y+=1
    if n % y == 0:
        return False
    else:
        return True
    
                
   