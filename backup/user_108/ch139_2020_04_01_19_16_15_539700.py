def arcotangente(x,n):
    sinal = -1
    soma = x
    lista = list(range(3,(3+(n-1)*2)+1,2))
    print(n,lista)
    for i in range(3,(3+(n-1)*2)+1,2):
        soma += (x**i/i) * sinal
        sinal = -sinal
    return soma
        