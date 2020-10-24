def lista_sufixos(p):
    a=[]
    c='a'
    for i in range(len(p)):
        c=p[i+1:]
        a.append(c)
    return a
        