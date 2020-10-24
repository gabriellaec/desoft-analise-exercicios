def calcula_euler(x,n):
    c = 0
    s = 0
    while(i<n):
        s += x**i/math.factorial(i)
        i += 1
    return s