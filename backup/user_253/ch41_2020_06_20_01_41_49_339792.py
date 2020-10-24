def zera_negativos(a):
    x=0
    for i in a:
        if i > 100:
            i=0
        a.insert(x, i)
        x+=1
    return (a)
    