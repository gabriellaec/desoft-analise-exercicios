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
    ex = 1
    i = 0
    while i < n:
        k = fatorial(i)
        ex += x**i/k
        i += 1
    return ex