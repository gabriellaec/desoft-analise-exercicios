def calcula_norma(vetor):
    norma = 0
    dentro = 0
    for i in vetor:
        dentro+=i**2
    norma = dentro**0.5
    return norma