def calcula_euler(x,n):
    k = 1
    calculo = 1 
    teste = True
    while teste:
        if (n) > k:
            calculo = calculo + (x**k)/k
            k = k + 1
        else:
            teste = False
    return calculo

