def calcula_fibonacci(x):
    F = [1,1]
    n = 1
    if x > 1:
        while n <= x-2:
            proximo = F[n] + F[n-1]
            F.append(proximo)
            n += 1
    return F