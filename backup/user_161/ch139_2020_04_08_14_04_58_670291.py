def arcotangente(x, n):
    i = 0
    indice = 1
    soma = 0
    while i < n:
        if i%2 == 0:
            soma += ((x**indice)/indice)
        else:
            soma -= ((x**indice)/indice)
        indice += 2
        i += 1
        
    return soma