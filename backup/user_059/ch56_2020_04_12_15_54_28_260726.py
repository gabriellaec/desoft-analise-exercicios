def calcula_norma(lista):
    norma = 0
    l = []
    for i in range(len(lista)):
        l.append(lista[i]**2)
    soma = sum(l)
    norma = soma**(1/2)
    return norma