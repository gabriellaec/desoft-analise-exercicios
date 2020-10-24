def interseccao_valores(x,y):
    l = []
    for e1 in x:
        for e2 in y:
            if x[e1] == y[e2]:
                l.append(x[e1])
    return l    
            