def lista_sufixos(p):
    l = []
    x = 0
    for i in range(len(p)):
        l.append(p[x: ])
        x+=1
    return l