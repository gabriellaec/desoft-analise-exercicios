def inverte_lista(l):
    i = 0
    lista = []
    while i in range(len(l)):
        lista.append(l[len(l)-i])
        i += 1
    return lista