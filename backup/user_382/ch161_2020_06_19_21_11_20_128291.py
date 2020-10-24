def PiWallis(n):
    num = 2
    den = 1 
    pi = 1 
    for i in range(1,n+1):
        pi *= num/den
        
        if i % 2 == 0:
            num+=2
        else:
            den+=2
    pi*= 2 
    return pi 
            
    
    