def classifica_lista(l):
    n = 'nenhum'
    c = 'crescente'
    d = 'decrescente'
    cresc = False
    decr = False
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
    
    if False not in cc:
        cresc = True
    elif False not in dd:
        decr = True
    if len(l) < 2:
        return n
    if cresc == True:
        return c
    elif decr == True:
        return d
    else:
        return n