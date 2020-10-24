def lista_sufixos(x):
    lista = []
    i = 0
    while i < len(x):
        lista.append(x)
        x = x[i:]
        i += 1
    return lista