def lista_sufixos(x):
    lista = [x]
    i = 0
    a = len(x)
    if x == '':
        lista = []
    else:
        while a>i:
            lista.append(x[i: ])
            i+=1
    return lista