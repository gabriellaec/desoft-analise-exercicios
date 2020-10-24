def lista_sufixos(a):
    x = len(a)
    z = a[2]
    lista = []
    i = 3
    p = ""
    b = 0
    while i < x:
        z = z + a[i]
        i += 1
        lista.append(p)
    p = ""
    lista.reverse()
    return lista