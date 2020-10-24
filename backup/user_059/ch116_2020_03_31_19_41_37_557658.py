def raiz_quadrada(x):
    i=1
    y = x
    cont = 0
    while y>0:
        y = y-i
        cont = cont+1
        i+=2
    return cont
