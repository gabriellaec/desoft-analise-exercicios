def eh_palindromo(x):
    inverso = ''
    a = len(x) - 1
    while a >= 0:
        letra = x[a]
        inverso = inverso + letra
        a = a - 1
    if inverso == x:
        resultado = True
    else:
        resultado = False
    return resultado