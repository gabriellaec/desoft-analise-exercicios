def calcula_euler(x,n):
    def fatorial(i):
        fatorial = 1
        while i != 1:
            fatorial *= i
            i -= 1
        return fatorial
    ex = 1
    for i in range(0,n):
        k = fatorial(i)
        ex += x**i/k
	return ex