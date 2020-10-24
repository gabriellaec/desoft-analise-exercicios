def calcula_euler(x,n):
    soma = 1
    expoente = 1
    f = 1
    while expoente < n:
        while f < expoente:
            f = expoente * f
            f += 1
        soma = soma + (x**expoente) / f
        expoente += 1
    return soma