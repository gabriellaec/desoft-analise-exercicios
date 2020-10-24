def fatorial(n):
    if n<=1:
        return (1)
    while n > 1:
        fatorial = fatorial*(n-1)
    return fatorial
