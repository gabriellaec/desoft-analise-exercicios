def calcula_pi(n):
    soma = 0
    i = 1
    while i < n:
        soma += 6/n**2
        n += 1
        i += 1
    return soma**(1/2)