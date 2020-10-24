def lista_primos(n):
    
    primes = list()
    current = 3
    if n > 0: primes.append(2)
    
    while len(primes) < n:
        
        for i in range(3, current + 1, 2):
            if i == current: primes.append(current)
            elif current % i == 0: break
        
        current += 2
   	
    return primes
        
            