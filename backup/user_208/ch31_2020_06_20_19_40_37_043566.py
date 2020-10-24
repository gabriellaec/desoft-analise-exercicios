def eh_primo (n):
    i = 2
    x = 0
    while (i <=(n/2)):
        while ((n%i)==0):
            x+=1
            break 
        i+=1
    if x == 0:
        return True
    else:
        return False
    
                
   