def calcula_norma(lista):
    norma = 0
    l = []
    for e in lista:
        l.append(lista[e]**2)
    soma = sum(l)
    norma = soma**1/2
    return norma
    