def calcula_pi (n):
    soma = 0
    for i in range (1, n + 1):
        soma += 6 / (i ** 2)
    pi = soma ** (1/2)
    return pi