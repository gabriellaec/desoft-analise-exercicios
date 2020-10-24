def lista_sufixos(a):
    x = len(a)
    lista = []
    i = 1
    p = ""
    b = 0
    while i < x:
        p = p + a[i]
        i += 1
        lista.append(p)
    p = ""
    lista.reverse()
    return lista