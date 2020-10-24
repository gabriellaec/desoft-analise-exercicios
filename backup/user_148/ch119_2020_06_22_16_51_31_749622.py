def calcula_euler(x, n):
    import math
    i = 0   
    while i<n:
        k = (x**i)/math.factorial(i)
        soma = 1 + k
        i += 1
        
    return soma
