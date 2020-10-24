def calcula_norma(vetor):
    norma = 0
    norma_real = norma**(0.5)
    for e in vetor:
        norma += e**2
    return norma_real