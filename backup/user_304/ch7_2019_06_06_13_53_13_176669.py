def calcula_norma(vetor):
    s=0
    for e in vetor:
        x=e**2
        s+=x
    norma=(s)**0.5
    return norma