def lista_sufixos(str):
    lista = []
    i = len(str)
    while i>=1:
        lista.append(str[-i:])
        i -= 1
    return lista
