def arcotangente (x, n):
    i = 1
    sinal = 1
    s = 0
    while i<=n:
        parcela = sinal*(x**i)/i
        s = s + parcela
        i = i + 2
        sinal = sinal*(-1)
        return s
