def calcula_norma(vetor):
    dimencao = len(vetor)
    soma = 0
    for i in vetor:
        soma += i**2
    norma = soma**(1/dimencao)
    return norma