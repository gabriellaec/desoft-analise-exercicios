def calcula_euler(x,n):
    euler = 1
    expoente = 1
    fatorial = 1
    while expoente < n:
        while f < expoente:
            f = expoente * f
            f += 1
        euler = (euler + (x**expoente) / f)
        expoente += 1
    euler = euler**1/x
    return euler