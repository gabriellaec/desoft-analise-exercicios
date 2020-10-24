def calcula_norma(lista):
    soma=0
    for i in lista:
        soma+=i**i
    return soma**(1/2)

        