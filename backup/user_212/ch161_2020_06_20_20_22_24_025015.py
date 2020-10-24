def PiWallis(n):
    i = 1
    conta = 1
    contador= 1
    while contador  < n :
        if i %2 == 0:
            conta = conta * ((i-1)/i)
            i+=2
            contador+=1
        elif i%2 != 0:
            conta = conta*((i+1)/i)
            i+=2
            contador += 1
        
    pi = (conta)*2
    return pi 
        
            
        