def raiz_quadrada(x):
    t = 0
    i = 1
    raiz = 0
    while(i < x):
        if i%2 != 0:
            raiz = x - i
        i += 1
        return raiz