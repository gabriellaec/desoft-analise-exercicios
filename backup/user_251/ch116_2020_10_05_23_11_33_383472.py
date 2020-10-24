def raiz_quadrada(a):
    numero = a
    i = 1
    resultado = 0
    while numero >= 0:
        numero -= i
        i += 2
        resultado += 1
        
    return resultado
        