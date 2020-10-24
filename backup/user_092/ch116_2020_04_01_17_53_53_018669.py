def raiz_quadrada(x):
    s = 1
    c = 0
    z = x
    while(z > 0):
        z = z - s
        c +=1
        s += 2
    return c