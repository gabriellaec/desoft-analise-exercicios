def raiz_quadrada(x):
    i= 1
    lista= []
    while i <= x:
        x= x - i
        lista.append(i)
        i= i + 2
    return len(lista)