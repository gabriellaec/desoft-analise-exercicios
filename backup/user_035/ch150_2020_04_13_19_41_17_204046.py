def calcula_pi(n):
    i = 1
    soma = 0
    while i <= n:
        pi = 6/(i**2)
        soma += pi
        i += 1
    soma_final = soma**(1/2)
    return soma_final