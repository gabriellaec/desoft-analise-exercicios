def calcula_euler(x, n):
    def fatorial(i):
        s = 1
        x = 1
        while 1 <= x <= n:
            s = s*x
            x = x + 1
        return s       
    i = 0
    y = 0
    while 0 <= i <= n:
        y += ((x**i)/fatorial(i))
        i += 1
    return y