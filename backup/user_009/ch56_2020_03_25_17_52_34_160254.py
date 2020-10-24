def calcula_norma(l):
    soma = 0
    for i in l:
        soma += i**2
    return soma**(1/2)