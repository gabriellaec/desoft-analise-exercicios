def PiWallis(n):
    i = 1
    conta = 1
    
    while i <= n :
        if i %2 == 0:
            conta = conta * ((i-1)/i)
            i+=2
        elif i%2 != 0:
            conta = conta*((i+1)/i)
            i+=2
        
    pi = conta *2
    return conta 
        
            
        