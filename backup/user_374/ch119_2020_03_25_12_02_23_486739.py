def calcula_euler(x,n):
    k = 1
    
    teste = True
    while teste:
        if (n+1) > k:
            calculo = 1 + (x**n)/k
            k = k + 1
        else:
            teste = False
    return calculo

