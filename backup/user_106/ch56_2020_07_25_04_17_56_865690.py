def calcula_norma (vetor):
    soma = 0
    for i in vetor:
        soma += i ** 2
    mod = soma ** 0.5
    return mod