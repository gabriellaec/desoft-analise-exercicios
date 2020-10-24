def raiz_quadrada(x):
    s = 1
    c = 0
    z = 1
    if x == 0:
        return 0
    else:
        while(z > 0):
            z += x - s
            c +=1
            s += 2
        return c