def fatorial(n):
    k = 0
    fatorial = 1
    if n == 0:
        return 1
    else:
        while k < n :
            fatorial = fatorial*(n-k)
            k += 1
    return fatorial
            