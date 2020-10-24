def raiz_quadrada(a) :
    i = 1
    contador = 1
    while i < a :
        contador += 1
        a -= i
        i += 2
    return contador


print(raiz_quadrada(2))
    
    