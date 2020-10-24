def classifica_lista(l):
    if len(l) <= 2:
        return 'nenhum'
    for i in range (len(l)):
        if l[i] > l[i-1]:
            c = True
        else:
            c = False
    if c == True:
        return 'crescente'
    else:
        return 'decrescente'
