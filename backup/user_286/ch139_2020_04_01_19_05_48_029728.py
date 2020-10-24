def arcotangente(x, n):
    lista = [x]
    contador = 3
    while len(lista) < n:
        if len(lista) % 2 != 0:
            lista.append(-1*x**contador/contador)
        else:
            lista.append(x**contador/contador)
        contador += 2

    
    return sum(lista)