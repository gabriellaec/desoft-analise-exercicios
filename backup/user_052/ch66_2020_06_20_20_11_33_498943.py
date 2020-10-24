def lista_sufixos (string):
    lista = []
    for i in string:
        x = string[i:]
        lista.append(x)
    return lista
        