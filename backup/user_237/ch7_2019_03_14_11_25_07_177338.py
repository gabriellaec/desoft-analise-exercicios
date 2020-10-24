def calcula_norma(vetor):
    norma = 0
    norma_quadrada = 0
    norma_raiz = 0
    for e in vetor:
        norma = e
        norma_quadrada += norma**2
    norma_raiz = norma_quadrada**(0.5)
    return norma_raiz