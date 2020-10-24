def lista_sufixos(x):
    l = []
    i = 0
    while i<len(x):
        l.append(x[i:])
        i+=1
    return l