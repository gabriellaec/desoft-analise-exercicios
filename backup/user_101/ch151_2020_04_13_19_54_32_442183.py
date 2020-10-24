def classifica_lista(l):
    n = 'nenhum'
    c = 'crescente'
    d = 'decrescente'
    cc = []
    dd = []
    for i, e in enumerate(l):
        if l[-1] == e:
            break
        else:
            if e < l[i+1]:
                cc.append(True)
            else:
                cc.append(False)
        if l[-1] == e:
            break
        else:
            if e > l[i+1]:
                dd.append(True)
            else:
                dd.append(False)
    print(cc)
    print(dd)
    if len(l) < 2:
        return n
    if False not in cc:
        return c
    elif False not in dd:
        return d
    else:
        return n

