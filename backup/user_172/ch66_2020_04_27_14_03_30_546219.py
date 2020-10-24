def lista_sufixos(x):
    lista = [x]
    i = 0
    if x == '':
        lista = []
    else:
        while i < len(x):
            del x[i]
            lista.append(x)
    print(lista)
    return lista