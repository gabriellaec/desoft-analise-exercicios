def raiz_quadrada(a) :
    i = 1
    s = a
    contador = 0
    while i < s :
        contador += 1
        s -= i
        i += 2
    return contador
    