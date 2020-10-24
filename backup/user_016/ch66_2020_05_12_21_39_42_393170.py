def lista_sufixos(a):
    lista = []
    i = 0
    while i < len(a):
        lista.append(a[i:])
        i += 1
    return lista