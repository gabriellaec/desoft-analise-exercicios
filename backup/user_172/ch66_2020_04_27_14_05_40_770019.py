def lista_sufixos(x):
    lista = [x]
    if x == '':
        lista = []
    else:
        while len(x)>1:
            lista.append(x[1: ])
    return lista