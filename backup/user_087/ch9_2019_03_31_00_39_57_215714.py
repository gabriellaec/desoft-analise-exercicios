def lista_sufixos(x):
    i=0
    lista = []
    while i < len(x):
        lista.append(x[i:])
        i += 1
    return lista
       