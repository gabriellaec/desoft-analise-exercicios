def encontra_maximo(matriz):
    a = matriz[0]
    b = matriz[1]
    c = matriz[2]
    i = 0
    while i < len(a):
        if a[0] >= a[1]:
            del a[1]
        else:
            del a[0]
        i += 1
    
    i = 0
    while i < len(b):
        if b[0] >= b[1]:
            del b[1]
        else:
            del b[0]
        i += 1
    
    i = 0
    while i < len(c):
        if c[0] >= c[1]:
            del c[1]
        else:
            del c[0]
        i += 1
    
    matriz_f = [a, b, c]
    i = 0
    while i < len(matriz_f):
        if matriz_f[0] >= matriz_f[1]:
            del matriz_f[1]
        else:
            del matriz_f[0]
        i += 1
    return matriz_f[0][0]