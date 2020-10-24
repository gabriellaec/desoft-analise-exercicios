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
    for i in range(0,n-1):
        k = fatorial(i)
        ex += x**i/k
        print(ex)
    return ex