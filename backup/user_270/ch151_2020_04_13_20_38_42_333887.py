def classifica_lista(l):
    i = 0
    t = 2
    up = 0
    down = 0
    if len(l) < 2:
        return 'nenhum'
    while i != len(l):
        if l[t-2] > l[t-1]:
            break
        else:
            up += 1
        i += 1
        t += 1
    while i != len(l):
        if l[t-2] < l[t-1]:
            break
        else:
            down += 1
        i += 1
        t += 1
    if up == (len(l)-1):
        return 'crescente'
    elif down == (len(l)-1):
        return 'decrescente'
    else:
        return'nenhum'