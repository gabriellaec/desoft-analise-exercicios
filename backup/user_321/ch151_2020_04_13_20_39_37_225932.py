def classifica_lista(l):
    c = 2
    for i in range (len(l)):
        if l[i] > l[i-1]:
            c = 0
        elif l[i] < l[i-1]:
            c = 1
        if (c == 0 and l[i] < l[i-1]) or (c == 1 and l[i] > l[i-1]):
            c = 2
            break
            
    if c == 0:
        return 'crescente'
    elif c == 1:
        return 'decrescente'
    elif c == 2:
        return 'nenhum'
