def classifica_lista(l):
    up = 0 
    down = 0
    if len(l) < 2:
        return 'nenhum'
    for i in range(0,len(l)):
        if l[i-1] < l[i] :
            down += 1
        elif l[i-1] > l[i] :
            up += 1
    if up == len(l)-1 :
        return 'crescente'
    elif down == len(l)-1 :
        return 'descrescente'
    else:
        return 'nenhum'