def lista_sufixos(string):
    lista = []
    i = 0
    while i < len(string):
        primeiro = string[i:]
        lista.append(primeiro)
        i += 1
    return lista    