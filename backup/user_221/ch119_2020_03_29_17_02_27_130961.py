def calcula_euler(x, n):
    def fatorial(i):
        s = 1
        x = 1
        while 1 <= x <= n:
            s = s*x
            x = x + 1
        return s       
    i = 1
    while 1 <= i <= n:
        y = 1 + ((x**i)/fatorial(i))
        i = i + 1
        return y