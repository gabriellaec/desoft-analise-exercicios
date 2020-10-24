def calcula_pi(n):
    i = 1
    soma = 0
    while i <= n:
        x = 6 / (i ** 2)
        soma += x
        i += 1
        pi = soma ** .5
    return pi