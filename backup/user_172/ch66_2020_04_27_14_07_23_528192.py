def lista_sufixos(x):
    lista = [x]
    a = len(x)
    if x == '':
        lista = []
    else:
        while a>1:
            lista.append(x[1: ])
            a-=1
    return lista