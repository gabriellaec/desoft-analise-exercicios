def calcula_euler(x, n):
    import math
    soma = 0
    i = 1
    
    while i<n:
        soma = soma + (x**i)/math.factorial(i)
        i += 1
        
    return soma
