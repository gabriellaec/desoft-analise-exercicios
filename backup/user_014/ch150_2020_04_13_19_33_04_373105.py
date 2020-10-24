def calcula_pi (n):
    i = 0
    soma = 0
    while i < n:
        soma = (soma + (6/(n**2))) ** 1/2
        i += 1
    return soma