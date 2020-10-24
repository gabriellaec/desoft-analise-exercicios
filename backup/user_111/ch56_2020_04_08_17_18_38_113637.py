def calcula_norma(vetor):
    y=0
    for i in vetor:
        y+=vetor[i]**2
    return y**(1/2)               