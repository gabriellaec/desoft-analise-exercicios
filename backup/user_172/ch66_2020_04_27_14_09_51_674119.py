def lista_sufixos(x):
    lista = [x]
    i = 0
    a = len(x)
    if x == '':
        lista = []
    elif a == 1:
        lista.append(x)
    elif a>1:
        while a>i:
            lista.append(x[i: ])
            i+=1
    return lista