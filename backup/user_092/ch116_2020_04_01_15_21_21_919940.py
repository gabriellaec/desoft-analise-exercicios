def raiz_quadrada(x):
    s = 1
    C = 1
    z = 1
    if x == 0:
        return 0
    else:
        while(z > 0):
            z += x - s
            C +=1
            s += 2
        return c