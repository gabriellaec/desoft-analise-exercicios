def estritamente_crescente(x):
    a = 1
    ultimo_maior = 0
    lista = []
    lena = len(x)
    while a < len(x):
        if x[a] > ultimo_maior:
            lista.append(x[a])
            ultimo_maior = x[a]
        a +=1
    return lista
