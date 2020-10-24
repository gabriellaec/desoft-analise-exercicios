def lista_sufixos(a):
    b = []
    for v in range(len(a)):
        b.append(a[v:])
    return b
