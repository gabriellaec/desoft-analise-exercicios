def calcula_pi(n):
    soma = 0
    i = 0
    while i < n:
        soma += 6/i**2
        i += 1
    return soma**(1/2)