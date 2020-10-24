def interseccao_valores(x,y):
    l = []
    for e1,e2 in zip(x,y):
        if x[e1] == y[e2]:
            l.append(x[e1])
    return l    
            