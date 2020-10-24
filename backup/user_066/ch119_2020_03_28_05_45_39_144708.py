def calcula_euler(x,n):
    def fatorial(i):
        if i == 0:
            fatorial = 1
        else:
            fatorial = 1
            while i != 1:
                fatorial *= i
                i -= 1
        return fatorial
    ex = 0
    if n == 0:
        ex = 1
    else:
        for i in range(n+1):
            k = fatorial(i)
            ex += x**i/k
    return ex