vetor = [1, 2, 3]

def calcula_norma (vetor):
    somaQuad = 0
    for e in vetor:
        somaQuad += e**2
    norma = somaQuad**(1/2)
    return norma
    