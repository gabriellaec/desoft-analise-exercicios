def arcotangente(x,n):
    i = 0
    v = 1
    resultado = 0
    a = 0
    while i < n:
        a = ((-1*i)*x**v)/v
        v += 2
        resultado += a
    return(resultado)