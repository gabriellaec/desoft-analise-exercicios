def classifica_lista(l):
    n = 'nenhum'
    c = 'crescente'
    d = 'decrescente'
    cc = []
    dd = []
    for i, e in enumerate(l):
        if l[i] == l[-1]:
            break
        else:
            if e < l[i+1]:
                cc.append(c)
            elif e > l[i+1]:
                cc.append(d)
    for i, e in enumerate(l):
        if l[-1] == l[i]:
            break
        else:
            if e > l[i+1]:
                dd.append(d)
            elif e < l[i+1]:
                dd.append(c)
    print(dd)
    if len(l) < 2:
        return n
    if d in cc and c in dd:
        return n
    elif d not in cc:
        return c
    elif c not in dd:
        return d

