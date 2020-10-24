def lista_sufixos(string):
    lista = []
    x = len(string)
    for i in range(x):
        lista.append(string[i:])
    return lista