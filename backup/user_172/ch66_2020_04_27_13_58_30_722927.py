def lista_sufixos(x):
    lista = [x]
    i = 0
    while i < len(x)-1:
        del x[i]
        lista.append(x)
        i=+1
    return lista