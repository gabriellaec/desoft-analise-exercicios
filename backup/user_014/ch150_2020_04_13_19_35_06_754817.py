def calcula_pi (n):
    i = 1
    soma = 6 ** 1/2
    while i <= n:
        soma = soma + ((6/(i**2))) ** 1/2
        i += 1
    return soma