def verifica_lista(l):
    i = False
    p = True
    if len(l) == 0:
        return 'misturado'
    for i in range(len(l)):
        if l[i]%2 != 0:
            p = False
            i = True
        elif l[i]%2 == 0:
            p = True
            i = False
    if i and not p:
        return 'ímpar'
    elif p and not i:
        return 'par'
    else:
        return 'misturado'           
