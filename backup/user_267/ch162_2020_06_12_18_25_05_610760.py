def verifica_lista(l):
        i = True
    p = True
    if len(l) == 0:
        return 'misturado'
    else:
        for i in range(len(l)):
            if l[i]%2 != 0:
                p = False
            elif l[i]%2 == 0:
                i = False
    if i:
        return 'ímpar'
    elif p:
        return 'par'
    else:
        return 'misturado'           
