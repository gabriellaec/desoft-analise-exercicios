def calcula_norma (vetor):
    x = 0
    while i<len(vetor):
        x += vetor[i]**2
        i+=1
    norma = x**(1/2)
    return norma