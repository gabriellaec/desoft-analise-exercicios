def lista_sufixos(string):
    sufx = []
    for i in range(0, len(string)):
        sufx.append(string[i:])
    return sufx