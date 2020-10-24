def arcotangente(x, n):
    i = 1
    resultado = 0
    while i<n and n>1:
        resultado = resultado + ((x**i)/i) -((x**(i+2))/(i+2))
        i +=4
return resultado
