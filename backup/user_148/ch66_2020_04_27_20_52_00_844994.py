def lista_sufixos(str):
    lista = []
    i = len(str)
    while i<len(str):
        lista.append(str[-i:])
        i += 1
    return lista
