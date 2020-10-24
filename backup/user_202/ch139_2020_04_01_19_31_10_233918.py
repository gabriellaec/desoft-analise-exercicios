def arcotangente(x,n):
    i = 0
    v = 1
    resultado = 0
    a = 0
    p = 0
    while i < n:
        if i%2 == 0:
            p = 1
        else:
            p = -1
        a = ((p)*x**v)/v
        v += 2
        i += 1
        resultado += a
    return(resultado)