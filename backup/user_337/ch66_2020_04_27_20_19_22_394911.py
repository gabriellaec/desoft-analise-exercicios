def lista_sufixos(string):
    lista = []
    i = 0
    while i < len(string):
        a = string[i::]
        lista.append(a)
        i += 1
    return lista