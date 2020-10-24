def maior_primo_menor_que (n):
    prime = False
    
    if n == 1 or n < 0:
        return(-1)
    else:
        while prime == False:
            for e in range(2,n):
                if n % e == 0:
                    n -= 1
                    prime = False
            prime = True
    return n 

