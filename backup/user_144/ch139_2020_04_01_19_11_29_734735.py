def arcotangente(x,n):
    i = 1
    soma = 0
    while i < n:
        soma += (x**(i)) / i 
        i += 1
        
    return soma