def arcotangente(x,n):
    i = 1
    soma = 0
    while i < n and  i %2 != 0:
        soma += x - ((x**i) / i )
        i += 1
        
    return soma