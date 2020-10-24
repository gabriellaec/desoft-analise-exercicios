def calcula_norma(lista):
    soma=0
    for a in lista:
        soma+=a**2
    modulo=soma**0.5
    return modulo