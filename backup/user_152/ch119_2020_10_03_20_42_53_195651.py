def calcula_euler (x, n):
    ex = 1
    ex += x
    fat = 1
    contador = 3
    while n+1 > contador:
        fat *= contador
        ex += (x**(n-1))/fat
        contador += 1
    return ex