def calcula_norma(lista):
    soma = 0
    for i in range(len(lista)):
        y = lista[i] ** 2
        soma += y
        i += 1
    soma_real = soma**(1/2)
    return soma_real