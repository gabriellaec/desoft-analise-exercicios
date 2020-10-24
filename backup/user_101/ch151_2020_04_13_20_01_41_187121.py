def classifica_lista(l):
    n = 'nenhum'
    c = 'crescente'
    d = 'decrescente'
    cc = []
    dd = []
    for i, e in enumerate(l):
        if e == l[-1]:
            break
        else:
            if e < l[i+1]:
                cc.append(c)
            else:
                cc.append(d)
    for i, e in enumerate(l):
        if l[-1] == e:
            break
        else:
            if e > l[i+1]:
                dd.append(d)
            else:
                dd.append(c)
    print(dd)
    if len(l) < 2:
        return n
    if d not in cc:
        return c
    elif c not in dd:
        return d
    else:
        return n

