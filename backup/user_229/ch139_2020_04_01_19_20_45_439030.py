def arcotangente(x,n):
    i = 1
    s = 0
    while i <= n:
        s += ((x**i)/i)*(-1)**(i-1)
        i += 2
    return s