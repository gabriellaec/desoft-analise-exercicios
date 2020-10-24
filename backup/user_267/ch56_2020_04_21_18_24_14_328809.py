def calcula_norma(n):
    i = 0
    soma = 0
    while i <= (len(n)-1):
        v = n[i]**2
        soma += v
        i += 1
    norma = soma**(1/2)
    return norma