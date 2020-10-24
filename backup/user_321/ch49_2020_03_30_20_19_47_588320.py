def inverte_lista(l):
    i = 1
    lista = []
    while i <= len(l):
        lista.append(l[len(l)-i])
        i += 1
    return lista