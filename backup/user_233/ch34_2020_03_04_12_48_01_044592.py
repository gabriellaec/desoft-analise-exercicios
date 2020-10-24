def maior_primo_menor_que(n):
    
    if n <= 2: return -1
    
    end = n + 1
    if n % 2 == 0: start = n
        
    primo = 2
    
    for i in range(3, start, 2):
        
        for j in range(3, i + 1):
            if j == i: primo = i
            if i % j == 0: break
    
    return primo
        
        
        
        