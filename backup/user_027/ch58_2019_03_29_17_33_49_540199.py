def calcula_fibonaci(x):
    F = [1,1]
    n = 1
    while n < x-1:
        proximo = F[n] + F[n-1]
        F.append(proximo)
        n += 1
    return F