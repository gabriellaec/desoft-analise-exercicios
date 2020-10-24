def lista_sufixos (string):
    lista = []
    i = 1
    lista.append(string)
    while i < len(string):
        x = string[i:]
        lista.append(x)
        i += 1
    return lista
        