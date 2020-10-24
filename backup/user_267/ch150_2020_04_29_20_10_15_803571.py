def calcula_pi(n):
    i = 1
    soma = 0
    while i <= n:
        i += 1
        soma += 6/i**2
    return soma**0.5