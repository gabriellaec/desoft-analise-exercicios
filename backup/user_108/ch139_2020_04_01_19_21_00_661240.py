def arcotangente(x,n):
    sinal = -1
    soma = x
    ultimo_i = 3+(n-2)*2
    for i in range(3,ultimo_i+1,2):
        soma += (x**i/i) * sinal
        sinal = -sinal
    return soma
        