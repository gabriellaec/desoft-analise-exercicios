def raiz_quadrada(x):
    i = 1
    raiz = 0
    while(i < x):
        if i%2 != 0:
            raiz += 1
        i += 1
    return raiz