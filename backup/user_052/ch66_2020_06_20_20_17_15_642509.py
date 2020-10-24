def lista_sufixos (string):
    lista = []
    i = 0
    while i < len(string):
        x = string[i:]
        lista.append(x)
        i += 1
    return lista
        