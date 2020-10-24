def calcula_norma(vetor):
    norma = 0
    print(vetor)
    for i, e in enumerate(vetor[1:]):
        if vetor[i] > vetor[i-1]:
            norma += (vetor[i] - vetor[i-1])
    return norma