def classifica_lista(l):
    up = 0 
    down = 0
    if len(l) < 2:
        return 'nenhum'
    i = 1
    for t in l:
        if l[i-1] < l[i] :
            down += 1
        elif l[i] > l[i+1] :
            up += 1
        i += 1
    if up == len(l)-1 :
        return 'crescente'
    elif down == len(l)-1 :
        return 'descrescente'
    else:
        return 'nenhum'