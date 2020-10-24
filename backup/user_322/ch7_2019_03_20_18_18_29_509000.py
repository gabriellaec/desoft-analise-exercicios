def calcula_norma(n):
    i = 0
    soma = 0
    a = 0
    while i < len(n) - 1:
        a = int(n[i])
        soma = soma + a ** 2
        i = i + 1
    norma = soma ** (1/2)
    return norma

