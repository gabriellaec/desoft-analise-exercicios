def arcotangente(x, n):
    a = 0
    i = 1
    resultado = 0
    while a<n n>1:
        resultado = resultado + ((x**i)/i) -((x**(i+2))/(i+2))
        i +=4
        a +=2
    return resultado