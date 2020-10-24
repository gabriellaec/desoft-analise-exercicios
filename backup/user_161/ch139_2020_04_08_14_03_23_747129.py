def arcotangente(x, n):
    i = 0
    indice = 1
    soma = 0
    sinal  = 1
    while i < n:
        soma += sinal * ((x**indice)/indice)
        indice += 2
        i += 1
        sinal *= -1
    return soma