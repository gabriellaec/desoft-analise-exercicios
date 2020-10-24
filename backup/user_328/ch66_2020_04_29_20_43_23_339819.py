def lista_sufixos(string):
    i= 0
    l= []
    while i < len(string):
        l.append(string[i:])
        i += 1
    return l