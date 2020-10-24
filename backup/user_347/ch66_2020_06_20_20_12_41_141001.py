def lista_sufixos(string):
    lista = []
    for a in range(len(string)):
        b = string[::(len(string)-a)]
        lista.append(b)
    return lista
    