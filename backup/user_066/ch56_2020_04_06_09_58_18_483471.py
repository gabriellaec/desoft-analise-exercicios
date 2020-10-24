def calcula_norma(vetor):
    dimencao = len(vetor)
    soma = 0
    for i in vetor:
        soma += (i[1]-i[0])**2
    norma = soma**(1/dimencao)
    print(norma)
    return norma