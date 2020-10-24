def arcotangente(x,n):
    i = 1
    s = 0
    z = 0
    while z < n:
        s += ((x**i)/i)*(-1)**(z)
        i += 2
        z += 1
    return s