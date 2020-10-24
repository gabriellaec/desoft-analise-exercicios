def calcula_euler(n):
    k = 1
    calculo = 1 
    teste = True
    while teste:
        if (n+1) > k:
            calculo = calculo + (n**k)/k
            k = k + 1
        else:
            teste = False
    return calculo

