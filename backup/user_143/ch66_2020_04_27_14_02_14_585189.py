def lista_sufixos(p):
    a=[]
    a.append(p)
    c='a'
    for i in range(len(p)):
        c=p[i+1:]
        a.append(c)
    del(a[len(a)])
    return a
        