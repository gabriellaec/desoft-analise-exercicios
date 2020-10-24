def arcotangente(x, n):
    i = 0
    indice = 1
    soma = 0
    sinal  = 1
    while i < n:
        if i%2 == 0:
            sinal = 1
        else:
            sinal = -1
        soma += sinal * ((x**indice)/indice)
        indice += 2
        i += 1
        
    return soma