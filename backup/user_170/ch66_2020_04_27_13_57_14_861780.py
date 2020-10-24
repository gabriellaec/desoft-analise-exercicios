def lista_sufixos(string):
    lista_sufixos = []
    for i in range(len(string)-1):
        lista_sufixos.append(string[:i])
    return lista_sufixos