def fatorial(n):
    i = 1
    
    N_fat = n
    
    while i < n:
        fat = n - i

        N_fat =N_fat*(fat)
        i += 1
        
    return N_fat