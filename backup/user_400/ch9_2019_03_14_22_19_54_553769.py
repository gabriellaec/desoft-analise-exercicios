def lista_sufixos(a):
    x = len(a)
    lista = []
    listaT = []
    i = 0
    c = 0
    while i < x:
        lista.append(a[i])
        i += 1
    h = len(lista)
    while c+1 < h:
        lista.remove(lista[0])
        listaT.append("".join(lista))
        c += 1
    return listaT