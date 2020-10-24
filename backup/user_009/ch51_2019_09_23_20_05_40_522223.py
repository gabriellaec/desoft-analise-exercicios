def estritamente_crescente(x):
    a = 1
    lista = []
    lena = len(x)
    while a < len(x):
        if x[a] > x[a-1]:
            lista.append(a)
        a +=1
    return lista