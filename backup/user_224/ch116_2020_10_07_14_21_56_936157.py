def raiz_quadrada(a) :
    i = 1
    contador = 1
    while i < a :
        contador += 1
        a -= i
        i += 2
        
    if a == 0:
        contador = 1
    return contador



    
    