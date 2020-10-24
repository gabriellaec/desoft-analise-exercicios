def arcotangente(x,n):
    sinal = -1
    soma = x
    for i in range(3,(3+n*2)+1,2):
        soma += (x**i/i) * sinal
        sinal = -sinal
    return soma
        