def agrupa_por_idade (d):
    c=[]
    t=[]
    a=[]
    i=[]
    dx= {'criança': c, 'adolecente': t, 'adulto': a, 'idoso': i }
    for x,y in d.items():
        if y<= 11:
            c.append(x)
        elif y>11 and y<=17:
            t.append(x)
        elif y> 17  and y< 60:
            a.append(x)
        else:
            i.append(x)
    return dx