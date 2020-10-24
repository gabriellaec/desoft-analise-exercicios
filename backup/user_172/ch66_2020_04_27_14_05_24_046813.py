def lista_sufixos(x):
    lista = [x]
    if x == '':
        lista = []
    else:
        while len(x)>0:
            lista.append(x[1: ])
    return lista