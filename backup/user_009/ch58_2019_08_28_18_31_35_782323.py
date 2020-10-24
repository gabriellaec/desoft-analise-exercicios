def calcula_fibonacci(n):
    lf = [0]*n
    x = 2
    lf[0] = 1
    lf[1] = 1
    while x <= (n - 1):
        lf[x] = lf[(x - 1)] + lf[(x - 2)]
        x += 1
calcula_fibonacci(n)
		