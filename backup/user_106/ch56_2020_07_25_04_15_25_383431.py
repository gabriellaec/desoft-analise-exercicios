def calcula_norma(vetor):
    if len(vetor) == 1:
        return vetor[0]
    elif len(vetor) == 2:
        mod = (vetor[0] ** 2 + vetor[1] ** 2) ** 0.5
        return mod
    else:
        mod = (vetor[0] ** 2 + vetor[1] ** 2 + vetor[2] ** 2) ** 0.5
        return mod