def lista_sufixos(string):
    if len(string) == 1:
        return [string]
    else:
        lista_sufixos = []
        for i in range(len(string)):
            lista_sufixos.append(string[i:])
        return lista_sufixos