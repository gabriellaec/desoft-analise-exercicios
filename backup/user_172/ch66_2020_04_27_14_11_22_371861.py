def lista_sufixos(x):
    lista = [x]
    i = 1
    a = len(x)
    if x == '':
        lista = []
    elif a == 1:
        lista = [x]
    elif a>1:
        while a>i:
            lista.append(x[i: ])
            i+=1
    return lista