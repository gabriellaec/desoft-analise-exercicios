def lista_sufixos(x):
    lista = [x]
    i = 0
    if x == '':
        lista = []
    else:
        while i < len(x):
            del (x[i])
            lista.append(x)
            i=+1
    return lista