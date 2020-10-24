def classifica_lista(l):
    if len(l) < 2:
        return 'nenhum'
    new_l = l
    new_l.append(l[-1])
    up = 0
    down = 0
    t = 1
    for i in l :
        if i > new_l[t] :
            down += 1
        elif i > new_l[t]:
            up += 1
        t += 1
    if up == len(l) :
        return 'crescente'
    elif down == len(l) :
        return 'decrescente'
    else:
        return 'nenhum'