def lista_sufixos(string):
    lista_sufixos = []
    while i < len(string):
        lista_sufixos.append(string(i:))
        i+=1
    return lista_sufixos
        