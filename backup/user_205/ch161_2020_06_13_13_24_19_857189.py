def PiWallis (n):
    i = 0
    k = 1 
    z = 2
    pi = 1
    while i <= n :
        pi *= (z**2/k**2)
        
        k +=2
        z +=2
        i+=1
    
    return 2*(pi)