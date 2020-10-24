def raiz_quadrada(x):
    i = 1
    lista = []
    while x != 0:
        x -= i
        lista.append(x)
        i += 2
    return len(lista)
        
        