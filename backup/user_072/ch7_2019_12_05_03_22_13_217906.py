def calcula_norma(lista):
    soma = 0
    for i in lista:
        soma = soma + i**2
    modulo = soma**(1/2)
    return modulo

print(calcula_norma([15,8]))