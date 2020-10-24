def calcula_tempo (n):
    pi = 0
    i = 1
    while i-1 < n:
        pi = (pi + 6/(i**2))**0.5
        i = i + 1    
    
    return pi