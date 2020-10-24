def maior_primo_menor_que(n):
    
    if n <= 2: return -1
    
    end = n + 1
    if n % 2 == 0: end = n
        
    if n == 2: return 2
    
    for i in range(3, end, 2):
        
        for j in range(3, i + 1):
            if j == i: primo = i
            if i % j == 0: break
    
    return primo
        
        
        
        