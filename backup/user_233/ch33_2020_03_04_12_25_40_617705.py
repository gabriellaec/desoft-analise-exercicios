def primos_entre(a, b):
    
    primes = 0
    
    start = a
    end = b + 1
    
    if a % 2 == 0:
        start = a + 1
    if b % 2 == 0:
        end = b
    
    for i in range(start, end, 2):
        
        for j in range(3, i + 1, 2):
            if j == i: primes += 1
            elif j % i == 0: break
                
    return primes
        
        
        
        
        