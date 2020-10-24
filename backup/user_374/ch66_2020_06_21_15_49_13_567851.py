def lista_sufixos(string):
    lista_sufixos = []
    for i in range(0, len(string)):
        lista_sufixos.append(string[i:])
    return lista_sufixos
