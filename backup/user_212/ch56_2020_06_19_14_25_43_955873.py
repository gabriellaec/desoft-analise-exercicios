def calcula_norma(lista):
    soma = 0
    for dim in lista:
        soma += dim**2
    norma = soma**(1/2)
    return norma