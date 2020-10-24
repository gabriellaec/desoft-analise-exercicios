def lista_sufixos(string):
    lista = []
    i = 0
    for e in string:
        a = string[i:len(string)]
        lista.append(a)
        i += 1
    return lista