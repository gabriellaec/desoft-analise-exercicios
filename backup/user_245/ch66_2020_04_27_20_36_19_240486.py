def lista_sufixos(string):
    a = []
    for i in range(len(string)-1,-1,-1):
        a.append(string[i:])
    return a