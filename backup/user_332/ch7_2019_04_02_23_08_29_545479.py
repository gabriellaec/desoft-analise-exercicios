def calcula_norma(lista):
    soma = 0
    for a in lista:
        soma += (a**2)
    mod = soma**(1/2)
    return(mod)