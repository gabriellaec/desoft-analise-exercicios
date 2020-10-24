def calcula_euler(x, n):
    i=0
    ex=0
    while i<=n:
        ex= ex + (x**i)/factorial(i)
    return ex   